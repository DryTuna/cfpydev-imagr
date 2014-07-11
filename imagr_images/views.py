from django.shortcuts import render
# from django.template import loader

from imagr_images.models import Image


def index(request):
    photos = Image.objects.all()
    context = {'photos' : photos}
    # template = loader.get_template('imagr_images/index.html')
    return render(request, 'imagr_images/index.html', context)


def photo(request, image_id):
    photo = Image.objects.get(pk=image_id)
    context = {'photo' : photo}
    return render(request, 'imagr_images/photos.html', context)


# u1 = User.objects.get(username="drytuna")
# albumn = u1.albumn_set.filter(photos__title__exact="Summer")
#             related set                    __contains=
