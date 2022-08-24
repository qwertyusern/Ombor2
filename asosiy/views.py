from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import *
from userapp.models import Ombor
from .serializers import *


class MahsulotVs(ModelViewSet):
    queryset = Mahsulot.objects.all()
    s=MahsulotSer
    def get_queryset(self):
        if Ombor.user==self.request.user:
            o = Mahsulot.objects.all()
        else:
            return Response()
    def post(self, request):
        if Ombor.user==self.request.user:
            ser = MahsulotSer(data=request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()
    def perform_update(self, serializer):
        if Ombor.user==self.request.user:
            serializer = MahsulotSer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response()
class Clientlar(generics.ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class = ClientSer
    def get_queryset(self):
        if Ombor.user==self.request.user:
            o = Client.objects.all()
        else:
            return Response()
    def post(self, request):
        if Ombor.user==self.request.user:
            ser = ClientSer(data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()
class ClientV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class =ClientSer
    def get_queryset(self):
        if Ombor.user==self.request.user:
            o = Client.objects.get(user=self.request.user)
        else:
            return Response()
    def perform_update(self, serializer):
        if Ombor.user==self.request.user:
            serializer = ClientSer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response()
