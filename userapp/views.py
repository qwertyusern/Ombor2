from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from asosiy.serializers import UserSer,OmborSer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from userapp.models import *




class OmborApi(APIView):
    def get(self, request,pk):
        o = Ombor.objects.get(user=self.request.user)
        ser=OmborSer(o)
        return Response(ser.data)

class Userlar(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

class UserV(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class = UserSer

