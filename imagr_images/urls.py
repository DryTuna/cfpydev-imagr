from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from imagr_images import views
from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView
from django.views.generic.base import TemplateView
from forms import ImagrUserRegistrationForm

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='registration/activation_complete.html'
        ),
        name='registration_activation_complete'),
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^activate/(?P<activation_key>\w+)/$',
        ActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/$',
        RegistrationView.as_view(form_class=ImagrUserRegistrationForm),
        name='registration_register'),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='registration/registration_complete.html'
        ),
        name='registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='registration/registration_closed.html'
        ),
        name='registration_disallowed'),
    (r'', include('registration.auth_urls')),
    url(r'^(?P<album_id>\d+)/$', views.album, name='album'),
    url(r'^(?P<image_id>\d+)/image_info/$', views.photo, name='photo'),
    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^(?P<username>\w+)/stream/$', views.stream, name='stream'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)