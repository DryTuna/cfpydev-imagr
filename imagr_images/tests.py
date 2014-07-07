from django.test import TestCase
from imagr_images.models import Image

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):
        Image.objects.create(title='image one')
        # Image.objects.create(title='image two', date_upl='07/02/2014')
        # Image.objects.create(title='image three', date_upl='07/01/2014')

    def test_image_title(self):
        i = Image.objects.get(title='image one')
        self.assertEqual(i.title, 'image one')
