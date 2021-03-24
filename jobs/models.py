from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to = 'Images/')
    summary = models.CharField(max_length = 200)