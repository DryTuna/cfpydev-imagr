from django.db import models


class Image(models.Model):
    image = models.FileField(upload_to='/photos/%Y/%m/%d')
    title = models.CharField(max_length=100)
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published', auto_now=True)
    privacy = models.IntegerField(choices=(('private', 0),
                                           ('public', 1),
                                           ))
    owner = models.ForeignKey('django.contrib.auth.models.User')

    def __unicode__(self):
        return self.title


class Albumn(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published', auto_now=True)
    privacy = models.IntegerField(choices=(('private', 0),
                                           ('public', 1),
                                           ))
    owner = models.ForeignKey('django.contrib.auth.models.User')
    photos = models.ForeignKey(Image)

    def __unicode__(self):
        return self.title
