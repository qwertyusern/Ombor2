from django.db import models

from asosiy.models import Mahsulot,Client

from userapp.models import Ombor

class Stats(models.Model):
    mahsulot=models.ForeignKey(Mahsulot,on_delete=models.SET_NULL,null=True)
    client=models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    umumiy=models.IntegerField()
    tolandi=models.IntegerField()
    miqdor=models.IntegerField()
    nasiya=models.IntegerField()
    foyda=models.IntegerField()
    sana=models.DateTimeField(auto_now_add=True)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)


