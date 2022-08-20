from django.db import models
from userapp.models import Ombor
class Mahsulot(models.Model):
    nom=models.CharField(max_length=50)
    brend=models.CharField(max_length=50)
    miqdor=models.SmallIntegerField()
    kelgan_narx=models.IntegerField()
    sotuv_narx=models.IntegerField()
    ombor=models.ForeignKey(Ombor,on_delete=models.CASCADE)

    def __str__(self):
        f"{self.nom} ({self.brend})"

class Client(models.Model):
    ism=models.CharField(max_length=70)
    tel=models.CharField(max_length=50)
    dokon=models.CharField(max_length=80)
    manzil=models.CharField(max_length=120)
    qarz=models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        f"{self.ism} ({self.dokon})"

