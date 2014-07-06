from django.db import models


class Image(models.Model):
    image = models.FileField(upload_to='/photos/%Y/%m/%d')
    title = models.CharField(max_length=100)
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published')
    privacy = models.IntegerField(choices=((0, 'private'),
                                           (1, 'public'),
                                           (2, 'shared')
                                           ))
    owner = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.title


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
    owner = models.ForeignKey('auth.User')
    images = models.ManyToManyField(Image)
    # cover = models.ForeignKey(Image)

    def __unicode__(self):
        return self.title


class Relate(models.Model):
    user_1 = models.ForeignKey('auth.User', related_name='one')
    user_2 = models.ForeignKey('auth.User', related_name='two')
    relation = models.IntegerField(choices=((0, 'None'),
                                            (1, '1 follow 2'),
                                            (2, '2 follow 1'),
                                            (3, 'Both')
                                            ))
    friend = models.IntegerField(choices=((0, 'No'), (1, 'Yes')))
