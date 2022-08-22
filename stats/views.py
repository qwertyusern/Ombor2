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
        if Ombor.user==self.request.user:
            o = Stats.objects.all()
        else:
            return Response("doc/")
class StatsV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stats.objects.all()
    serializer_class =StatsSer
    def get_queryset(self):
        if Ombor.user==self.request.user:
            o = Stats.objects.get(user=self.request.user)
        else:
            return Response("doc/")

