from django.db import models

class Work(models.Model):
    title = models.CharField(max_length= 260)
    post_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'Images/')
