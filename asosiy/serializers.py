from django.contrib.auth.models import User

from .models import *
from userapp.models import Ombor
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


s=serializers.ModelSerializer
class OmborSer(s):
    class Meta:
        model=Ombor
        fields="__all__"

class MahsulotSer(s):
    class Meta:
        model=Mahsulot
        fields="__all__"

class ClientSer(s):
    class Meta:
        model=Client
        fields="__all__"

class UserSer(s):
    class Meta:
        model=User
        fields="__all__"
