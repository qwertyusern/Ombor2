from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.models import Ombor
from asosiy.serializers import StatsSer
from . models import *

class StatsApiView(APIView):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["mahsulot", "client","sana"]
    ordening_fields = ["sana"]
    def get(self,request):
        o=Ombor.objects.get(user=request.user)
        s=Stats.objects.filter(ombor=o)
        ser=StatsSer(data=s)
        return Response(ser.data)
    def post(self, request):
        malumot=request.data
        ser = StatsSer(data=malumot)
        if ser.is_valid():
            o=Ombor.objects.get(user=request.user)
            ser.save(ombor=o)
        return Response(ser.data)
class StatsApi(APIView):
    def get(self,request,pk):
        o = Ombor.objects.get(user=request.user)
        s=Stats.objects.filter(id=pk,ombor=o)
        ser=StatsSer(s)
        return Response(ser.data)
    def put(self, request,pk):
        o = Ombor.objects.get(user=request.user)
        s=Stats.objects.get(id=pk)
        if s.ombor==o:
            malumot=request.data
            ser = StatsSer(s,data=malumot)
            if ser.is_valid():
                ser.save(ombor=o)
            return Response(ser.data)
        return Response()

