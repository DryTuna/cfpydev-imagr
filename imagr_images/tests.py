from django.test import TestCase


class ImagrImagesTest(TestCase):
    def test_index_view_with_no_image(self):
        response = self.client.get(reverse('imagr_images:index'))
