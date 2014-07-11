# import datetime

# from django.utils import timezone
import os
import sys
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from imagr_images.models import Relationship, ImagrUser, Image, Album


class ImageTests(TestCase):

    def setUp(self):
        """Create a user and image that can be used in all tests.

        Create a temp folder for images to be stored in, so test images
        don't clog up regular media folder."""

        TEST_ROOT = os.path.abspath(os.path.dirname(__file__))

        self._old_MEDIA_ROOT = settings.MEDIA_ROOT

        # override MEDIA_ROOT for this test
        settings.MEDIA_ROOT = os.path.join(TEST_ROOT, 'testdata/media/')

        user = ImagrUser(username="nathan")
        user.save()

        with open("/home/nathan/Pictures/codeschool.png", 'rb') as fi:
            an_image = File(fi)
            image = Image(title=u"Nathan's Photo", image=an_image,
                          privacy=0, owner=user)
            image.save()

        album = Album(title="Nathan's Album")

    def tearDown(self):
        # reset MEDIA_ROOT
        settings.MEDIA_ROOT = self._old_MEDIA_ROOT

    def test_image_has_title(self):
        """
        Test an image is properly represented by its title.
        """
        image = Image.objects.get(title="Nathan's Photo")
        self.assertEqual(unicode(image), u"Nathan's Photo")
