from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from asosiy.serializers import UserSer,OmborSer
from rest_framework.viewsets import ModelViewSet
from .models import *

class OmborVs(ModelViewSet):
    queryset = Ombor.objects.all()
    s=OmborSer

class Userlar(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

class UserV(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

