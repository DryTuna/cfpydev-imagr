from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q


FOLLOWING_BITS = {
    'left': 1,
    'right': 2
}


class Relationship(models.Model):
    user_1 = models.ForeignKey('imagr_users.ImagrUser', related_name='one')
    user_2 = models.ForeignKey('imagr_users.ImagrUser', related_name='two')
    relation = models.IntegerField(choices=(
        (0, 'none'),
        (1, '1 follows 2'),
        (2, '2 follows 1'),
        (3, 'both')
    ))
    friendship = models.IntegerField(choices=(
        (0, 'no'),
        (1, '1 request 2'),
        (2, '2 request 1'),
        (3, 'yes'),
        (4, '1 blocked 2'),
        (8, '2 blocked 1')
    ))

    class Meta:
        unique_together = ('one', 'two')

    def __unicode__(self):
        symbol = FOLLOWER_SYMBOLS.get(self.follower_status, ' - ')
        representation = u'{} {} {}'.format(
            unicode(self.left), symbol, unicode(self.right))
        if self.friendship:
            representation = representation.replace(u'-', u'F')
        return representation

    def clean(self):
        one = self.user_1
        two = self.user_2
        one_two = Q(one=one) & Q(two=two)
        two_one = Q(one=two) & Q(two=one)
        if self.__class__.objects.filter(Q(one_two | two_one)).exists():
            msg = u"A relationship already exists between {} and {}"
            raise ValidationError(msg.format(one, two))


class ImagrUser(AbstractUser):
    relationship = models.ManyToManyField(
        'imagr_users.ImagrUser',
        related_name="+",
        symmetrical=False,
        through='imagr_users.Relationship',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = u'user'
        verbose_name_plural = u'users'

    def __unicode__(self):
        if self.first_name and self.last_name:
            name = self.get_full_name()
        else:
            name = self.username
        return name

    def friends(self):
        iam_1 = (
            Q(one__user_1 = self) &
            Q(one__relation__in = 3)
        )
        iam_2 = (
            Q(two__user_2 = self) &
            Q(two__relation__in = 3)
        )
        frnds = ImagrUser.objects.filter(
            Q(iam_1 | iam_2)
        )
        return frnds

    def followers(self):
        iam_1 = (
            Q(one__user_1 = self) &
            Q(one__relation__in = [2, 3])
        )
        iam_2 = (
            Q(two__user_2 = self) &
            Q(two__relation__in = [1, 3])
        )
        followers = ImagrUser.objects.filter(
            Q(iam_1 | iam_2)
        )
        return followers

    def following(self):
        iam_1 = (
            Q(one__user_1 = self) &
            Q(one__relation__in = [1, 3])
        )
        iam_2 = (
            Q(two__user_2 = self) &
            Q(two__relation__in = [2, 3])
        )
        following = ImagrUser.objects.filter(
            Q(iam_1 | iam_2)
        )
        return following

    def follow(self, other):
        if other not in self.following():
            rel = self._get_rel(other)
            if rel is not None:
                for slot in ['one', 'two']:
                    if getattr(rel, slot) == self:
                        bitmask = FOLLOWING_BITS[slot]
                        rel.relation = rel.relation | bitmask
                        break
            else:
                rel = Relationship(
                    one=self, two=other, relation=1
                )
            rel.full_clean()
            rel.save()

    def unfollow(self, other):
        if other not in self.following():
            return
        rel = self._get_rel(other)
        if rel is not None:
            for slot in ['one', 'two']:
                if getattr(rel, slot) == self:
                    bitmask = FOLLOWING_BITS[slot]
                    rel.relation = rel.relation & ~bitmask
                    rel.full_clean()
                    rel.save()
                    return

    def _get_rel(self, other):
        rel = None
        try:
            rel = Relationship.objects.get(one=self, two=other)
        except Relationship.DoesNotExist:
            try:
                rel = Relationship.objects.get(one=other, two=self)
            except Relationship.DoesNotExist:
                pass
        return rel
