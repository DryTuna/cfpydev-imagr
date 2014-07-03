from django.db import models


class Image(models.Model):
    image = models.FileField(upload_to='/photos/%Y/%m/%d')
    title = models.CharField(max_length=100)
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published')
    privacy = models.IntegerField(choices=(('private', 0),
                                           ('public', 1),
                                           ('shared', 2)
                                           ))
    owner = models.ForeignKey('auth.User')

    def __unicode__(self):
        return self.title


class Albumn(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_upl = models.DateTimeField('date uploaded', auto_now_add=True)
    date_mod = models.DateTimeField('date modified', auto_now=True)
    date_pub = models.DateTimeField('date published')
    privacy = models.IntegerField(choices=(('private', 0),
                                           ('public', 1),
                                           ('shared', 2)
                                           ))
    owner = models.ForeignKey('auth.User')
    images = models.ManyToManyField(Image)
    # cover = models.ForeignKey(Image)

    def __unicode__(self):
        return self.title


class Relate(models.Model):
    user1 = models.ForeignKey('auth.User')
    user2 = models.ForeignKey('auth.User')
    relation = models.IntegerField(choices=(('none', 0),
                                            ('1 follow 2', 1),
                                            ('2 follow 1', 2),
                                            ('both', 3)
                                            ))
    friend = models.IntegerField(choices=(('no', 0), ('yes', 1)))
