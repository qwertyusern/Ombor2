from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class MahsulotVs(ModelViewSet):
    queryset = Mahsulot.objects.all()
    s=MahsulotSer
class Clientlar(generics.CreateAPIView):
    queryset=Client.objects.all()
    serializer_class = ClientSer

class ClientV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class =ClientSer
