from django.conf import settings
from django.db import models


class Image(models.Model):
    image = models.ImageField('The Image', upload_to='photos/%Y/%m/%d')
    title = models.CharField(max_length=128)
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
    title = models.CharField(max_length=128)
    description = models.TextField()
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published')
    privacy = models.IntegerField(choices=((0, 'private'),
                                           (1, 'public'),
                                           (2, 'shared')
                                           ))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    images = models.ManyToManyField(
        Image,
        related_name="albums",
        blank=True,
        null=True,
    )
    cover_photo = models.ManyToManyField(
        Image,
        related_name="cover_of",
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.title
