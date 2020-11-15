from django.db import models

class loradata(models.Model):
    phValue = models.CharField(max_length=100)
    doValue = models.CharField(max_length=100)
    orpValue = models.CharField(max_length=100)
    tdsValue = models.CharField(max_length=100)
    turValue = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    key = models.CharField(max_length=100, default="ASIA")
    latitude = models.CharField(max_length=100, default="36.35111")
    longitude = models.CharField(max_length=100, default="127.38500")
    name = models.CharField(max_length=100, default="Daejeon")


