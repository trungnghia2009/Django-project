from django.db import models

# Create your models here.

class Build(models.Model):
    title = models.CharField(max_length=255)
    upload = models.FileField(upload_to='upload/')