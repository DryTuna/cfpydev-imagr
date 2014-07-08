from django.db import models


class Image(models.Model):
    image = models.FileField(upload_to='photos/%Y/%m/%d')
    title = models.CharField(max_length=128)
    height = models.PositiveSmallIntegerField(default=0, editable=False)
    width = models.PositiveSmallIntegerField(default=0, editable=False)
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published')
    privacy = models.PositiveSmallIntegerField(choices=((0, 'private'),
                                                        (1, 'public')
                                                        ))
    owner = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.title


class Albumn(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published')
    privacy = models.IntegerField(choices=((0, 'private'),
                                           (1, 'public'),
                                           ))
    owner = models.ForeignKey('auth.User')
    images = models.ManyToManyField(
        Image,
        related_name="albumns",
        blank=True,
        null=True,
    )
    cover = models.ManyToManyField(
        Image,
        related_name="cover",
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.title
