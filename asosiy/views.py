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
        o=Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            Mahsulot.objects.filter(ombor=o)
        else:
            return Response()
    def post(self, request):
        o = Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            m=Mahsulot.objects.create()
            ser = MahsulotSer(m,data=request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()
    def update(self, request, pk):
        o = Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            m = Mahsulot.objects.get(id=pk).update()
            ser = MahsulotSer(m,data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()
class Clientlar(generics.ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class = ClientSer
    def get_queryset(self):
        o = Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            Client.objects.filter(ombor=o)
        else:
            return Response()
    def post(self, request):
        o = Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            c = Client.objects.create()
            ser = ClientSer(c,data=self.request.data)
            if ser.is_valid():
                ser.save()
            return Response(ser.data)
        return Response()
class ClientV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class =ClientSer
    def retrieve(self, request, pk):
        o = Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            Client.objects.get(id=pk)
        else:
            return Response()
    def update(self, request,pk):
        o = Ombor.objects.get(user=self.request.user)
        if o.user==self.request.user:
            c=Client.objects.get(id=pk).update()
            serializer = ClientSer(c,data=self.request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response()
