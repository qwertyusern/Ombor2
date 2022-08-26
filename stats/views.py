from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.response import Response
from userapp.models import Ombor
from asosiy.serializers import StatsSer
from . models import *

class StatsView(generics.ListCreateAPIView):
    queryset=Stats.objects.all()
    serializer_class = StatsSer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["mahsulot", "client","sana"]
    ordening_fields = ["sana"]
    def get_queryset(self):
        o=Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            Stats.objects.filter(ombor=o)
        else:
            return Response()
    def post(self, request):
        o = Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            s=Stats.objects.create()
            ser = StatsSer(s,data=request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()
class StatsV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stats.objects.all()
    serializer_class =StatsSer
    def retrieve(self,request,pk):
        o = Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            Stats.objects.get(id=pk)
        else:
            return Response()
    def update(self, request,pk):
        o = Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            s=Stats.objects.update(id=pk)
            serializer = StatsSer(s,data=self.request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response()

