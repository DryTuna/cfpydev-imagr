from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.template import loader

from imagr_images.models import Image


def index(request):
    photos = Image.objects.all()
    context = {'photos' : photos}
    # template = loader.get_template('imagr_images/index.html')
    return render(request, 'imagr_images/index.html', context)

@login_required(login_url='/accounts/login/')
def photo(request, image_id):
    photo = Image.objects.get(pk=image_id)
    context = {'photo' : photo}
    return render(request, 'imagr_images/photos.html', context)


def authentication(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'imagr_images/photos.html')
        else:
            return render(request, 'registration/logout.html')
    else:
        return render(request, 'registration/logout.html')


def logout_view(request):
    logout(request)


# u1 = User.objects.get(username="drytuna")
# albumn = u1.albumn_set.filter(photos__title__exact="Summer")
#             related set                    __contains=
