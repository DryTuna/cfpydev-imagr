from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File


class Image(models.Model):
    image = models.ImageField('The Image', upload_to='photos/%Y/%m/%d')
    title = models.CharField(max_length=100)
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published')
    privacy = models.IntegerField(choices=((0, 'private'),
                                           (1, 'public'),
                                           (2, 'shared')
                                           ))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.title

    def size(self):
        return self.image.size
    # # def image_size(self):
    # f = open(image.name, 'rb')
    # my_file = File(f)
    # image_size = my_file.size

    def published_between(self, start, end):
        return start < self.date_pub < end
    published_between.boolean = True
    published_between.short_description = 'Published Between...?'


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published')
    privacy = models.IntegerField(choices=((0, 'private'),
                                           (1, 'public'),
                                           (2, 'shared')
                                           ))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    images = models.ManyToManyField(Image)
    # cover = models.ForeignKey(Image)

    def __unicode__(self):
        return self.title


# class Relate(models.Model):
#     user_1 = models.ForeignKey('auth.User', related_name='one')
#     user_2 = models.ForeignKey('auth.User', related_name='two')
#     relation = models.IntegerField(choices=((0, 'None'),
#                                             (1, '1 follow 2'),
#                                             (2, '2 follow 1'),
#                                             (3, 'Both')
#                                             ))
#     friend = models.IntegerField(choices=((0, 'No'), (1, 'Yes')))
