from django.contrib import admin
from imagr_images.models import Image, Album, Relate
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('date_upl', 'date_mod')
    list_display = ('title', 'owner', 'image')
    list_filter = ('date_upl',)

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('date_upl', 'date_mod')
    list_display = ('title', 'owner',)

admin.site.register(Image, ImageAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Relate)
