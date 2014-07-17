from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from imagr_images.models import Image, ImagrUser, Album


def index(request):
    photos = Image.objects.all()
    users = ImagrUser.objects.all()
    context = {'photos' : photos,
               'users' : users,}
    # template = loader.get_template('imagr_images/index.html')
    return render(request, 'imagr_images/index.html', context)


@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = ImagrUser.objects.get(username=username)
    albumns = Album.objects.filter(owner=user)
    photos = []
    photos = Image.objects.filter(owner=user)
    context = {'albumns': albumns,
               'photos' : photos,
               'full_name': username}
    return render(request, 'imagr_images/profile.html', context)


@login_required(login_url='/accounts/login/')
def album(request, album_id):
    album = Album.objects.get(pk=album_id)
    photos = album.images.all()
    context = {'photos' : photos,
               'album_id' : album_id,
               'title': album.title}
    return render(request, 'imagr_images/album.html', context)


@login_required(login_url='/accounts/login/')
def photo(request, image_id):
    photo = Image.objects.get(pk=image_id)
    context = {'image': photo.image.url,
               'title': photo.title,
               'uploaded': photo.date_upl,
               'owner_name': photo.owner.username,
               'username': photo.owner.username,}
    return render(request, 'imagr_images/photo.html', context)


@login_required(login_url='/accounts/login/')
def stream(request, username):
    user = ImagrUser.objects.get(username=username)
    friends = user.friends()
    followings = user.following()
    result = []
    for i in list(friends | followings):
        pix = Image.objects.filter(owner=i).order_by('date_upl')[0]
        result.append(pix)
    context = {'photos' : result}
    return render(request, 'imagr_images/stream.html', context)


def logout_view(request):
    logout(request)


# u1 = User.objects.get(username="drytuna")
# albumn = u1.albumn_set.filter(photos__title__exact="Summer")
#             related set                    __contains=
