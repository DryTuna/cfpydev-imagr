from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

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


class Albumn(models.Model):
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
    relation = models.IntegerField(choices=((0, 'none'),
                                            (1, '1 follows 2'),
                                            (2, '2 follows 1'),
                                            (3, 'both')
                                            ))
    friendship = models.IntegerField(choices=((0, 'no'),
                                              (1, '1 request 2')
                                              (2, '2 request 1')
                                              (3, 'yes')
                                              (4, '1 blocked 2')
                                              (8, '2 blocked 1')
                                              ))


class ImagrUser(AbstractUser):

    def followers(self):
        iam_1 = (
            Q(one__user_1 = self) &
            Q(one__relation__in = [2, 3])
            )
        iam_2 = (
            Q(two__user_2 = self) &
            Q(two__relation__in = [1, 3])
            )
        my_followers = ImagrUser.objects.filter(
            Q(iam_1 | iam_2)
            )
        return my_followers

    def follow(self, other):
        raise NotImplementedError

    def unfollow(self, other):
        raise NotImplementedError
