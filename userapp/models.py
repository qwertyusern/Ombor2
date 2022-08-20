from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    ism=models.CharField(max_length=60)
    tel=models.CharField(max_length=50)
    dokon=models.CharField(max_length=70)
    manzil=models.CharField(max_length=120)
    user=models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.ism} ({self.dokon})'
