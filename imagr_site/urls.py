from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from imagr_images import views
# from imagr_site.views import HomePageView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imagr_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$',
    #     HomePageView.as_view(),
    #     name='home'
    # ),
    # url(r'^templates/imagr_images/photos.html', views.photos, name='photos'),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<album_id>\d+)/$', views.album, name='album'),
    url(r'^(?P<image_id>\d+)/image_info/$', views.photo, name='photo'),
    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^(?P<username>\w+)/stream/$', views.stream, name='stream'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
