from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from userapp.models import Ombor
from .serializers import *


class MahsulotApiView(APIView):
    def get(self,request):
        o=Ombor.objects.get(user=request.user)
        m=Mahsulot.objects.filter(ombor=o)
        ser=MahsulotSer(m,many=True)
        return Response(ser.data)
    def post(self, request):
        malumot=request.data
        ser = MahsulotSer(data=malumot)
        if ser.is_valid():
            o = Ombor.objects.get(user=request.user)
            ser.save(ombor=o)
        return Response(ser.data)
class MahsulotApi(APIView):
    def put(self, request, pk):
        o = Ombor.objects.get(user=request.user)
        mahsulot = Mahsulot.objects.get(id=pk)
        if mahsulot.ombor == o:
            malumot=request.data
            ser = MahsulotSer(data=malumot)
            if ser.is_valid():
                ser.save(ombor=o)
            return Response(ser.data)
        return Response()
class ClientApiView(APIView):
    def get(self,request):
        o = Ombor.objects.get(user=request.user)
        c=Client.objects.filter(ombor=o)
        ser = ClientSer(c, many=True)
        return Response(ser.data)
    def post(self, request):
        malumot = request.data
        ser = ClientSer(data=malumot)
        if ser.is_valid():
            o = Ombor.objects.get(user=request.user)
            ser.save(ombor=o)
        return Response(ser.data)
class ClientApi(APIView):
    def get(self, request, pk):
        o = Ombor.objects.get(user=request.user)
        c=Client.objects.get(id=pk,ombor=o)
        ser=ClientSer(c)
        return Response(ser.data)
    def put(self, request,pk):
        o = Ombor.objects.get(user=request.user)
        client = Client.objects.get(id=pk)
        if client.ombor == o:
            malumot = request.data
            ser = MahsulotSer(data=malumot)
            if ser.is_valid():
                ser.save(ombor=o)
            return Response(ser.data)
        return Response()