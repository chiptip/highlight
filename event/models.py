from django.db import models

# Create your models here.

class Event(models.Model):
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
