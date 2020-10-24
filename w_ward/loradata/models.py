from django.db import models

class loradata(models.Model):
    phValue = models.CharField(max_length=100)
    doValue = models.CharField(max_length=100)
    orpValue = models.CharField(max_length=100)
    tdsValue = models.CharField(max_length=100)
    turValue = models.CharField(max_length=100)



