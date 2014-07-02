from django.db import models

class Image(models.Model):
    image = models.FileField()
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField('date uploaded')


class Albumn(models.Model):
    Photos = models.ForeignKey(Image)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField('date uploaded')
