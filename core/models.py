from django.db import models

# Create your models here.
class Video(models.Model):
    source_url = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
