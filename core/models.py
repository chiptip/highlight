from django.db import models

# Create your models here.
class Download(models.Model)
    url = models.CharField(max_length=255)

