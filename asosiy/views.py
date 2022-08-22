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
            return Response("doc/")
class Clientlar(generics.ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class = ClientSer
    def get_queryset(self):
        if Ombor.user==self.request.user:
            o = Client.objects.all()
        else:
            return Response("doc/")
class ClientV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class =ClientSer
    def get_queryset(self):
        if Ombor.user==self.request.user:
            o = Client.objects.get(user=self.request.user)
        else:
            return Response("doc/")