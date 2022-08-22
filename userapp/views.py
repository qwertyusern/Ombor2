from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from asosiy.serializers import UserSer,OmborSer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from userapp.models import *




class OmborGet(generics.RetrieveAPIView):
    queryset = Ombor.objects.all()
    s=OmborSer
    def get_queryset(self):
        if Ombor.user==self.request.user:
            o = Ombor.objects.get(user=self.request.user)
        else:
            return Response("doc/")

class Userlar(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

class UserV(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

