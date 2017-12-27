import time
import json
import jwt

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from weixin.lib.wxcrypt import WXBizDataCrypt
from weixin.client import WeixinAPI,WXAPPAPI
from weixin.oauth2 import OAuth2AuthExchangeError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserRegSerializer
# Create your views here.

APP_ID = 'wx4636235cedd530c5'
APP_SECRET = 'b2b82875c211448885191e7f7efd091f'


class UserViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    def get_serializer_class(self):
        if self.action == "create":
            return UserRegSerializer
        return UserRegSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        #user = self.perform_create(serializer)
        user = User(username=request.data.username, password=request.data.password, gender=request.data.gender,
                    avatarUrl=request.data.avatarUrl)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status = status.HTTP_201_CREATED, headers=headers)

def get_wxapp_userinfo(encrypted_data, iv, code):
    '''
    换取openid和session_key
    :param encrypted_data:
    :param iv:
    :param code:
    :return:
    '''
    api = WXAPPAPI(appid=APP_ID,
                    app_secret=APP_SECRET)
    try:
        session_info = api.exchange_code_for_session_key(code=code)
    except OAuth2AuthExchangeError as e:
        return None
    session_key = session_info.get('session_key')
    crypt = WXBizDataCrypt(APP_ID,session_key)

    user_info = crypt.decrypt(encrypted_data, iv)
    return user_info


def addUser(userInfo):
    '''
    判断是否存在，如果不存在，添加用户
    :param userInfo:
    :return:
    '''
    openid = userInfo.get('openId', None)
    user = User.objects.get(openid=openid)
    id = user.id
    nickname = user.nickname
    if not user:
        nickname = userInfo.get('nickName', None)
        gender = userInfo.get('gender', None)
        avatarUrl = userInfo.get('avatarUrl', None)

        user = User(openid=openid, nickname=nickname, gender=gender, avatarUrl=avatarUrl)
        user.save()
    token = Token.objects.get_or_create(user_id = user.id)
    return token[0]

def login(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        code = req['code']
        encrypted_data = req['encryptedData']
        iv = req['iv']

        user_info = get_wxapp_userinfo(encrypted_data, iv, code)
        token = addUser(user_info)

        return HttpResponse(json.dumps(token.key), content_type='application/json')
