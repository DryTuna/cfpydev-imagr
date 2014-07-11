from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# from django.template import loader

from imagr_images.models import Image, ImagrUser, Album


def index(request):
    photos = Image.objects.all()
    context = {'photos' : photos}
    # template = loader.get_template('imagr_images/index.html')
    return render(request, 'imagr_images/index.html', context)


@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = ImagrUser.objects.get(username=username)
    albumns = Album.objects.filter(owner=user.pk)
    context = {'albumns': albumns}
    return render(request, 'imagr_images/profile.html', context)


@login_required(login_url='/accounts/login/')
def photo(request, album_id):
    album = Album.objects.get(pk=album_id)
    photos = album.images.all()

    context = {'photos' : photos}
    return render(request, 'imagr_images/photos.html', context)


def logout_view(request):
    logout(request)


# u1 = User.objects.get(username="drytuna")
# albumn = u1.albumn_set.filter(photos__title__exact="Summer")
#             related set                    __contains=
