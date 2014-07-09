from django.contrib import admin
from imagr_images.models import Image, Album, ImagrUser, Relationship
# Register your models here.


class PhotoSizeFilter(admin.SimpleListFilter):
    title = "File Size"
    parameter_name = "size"

    def lookups(self, request, model_admin):
        return (
            ('0', "=< 1MB"),
            ('1', "1 MB < 10 MB"),
            ('2', "10MB < 100MB"),
            ('3', "> 100MB"),
        )

    def queryset(self, request, queryset):
        if self.value() == 'All':
            return queryset
        if self.value() == '0':
            return queryset.filter(size__lte=1048576)
        if self.value() == '1':
            return queryset.filter(
                size__lte=10485760, size__gt=1048576
            )
        if self.value() == '2':
            return queryset.filter(
                size__lte=104857600, size__gt=10485760
            )
        if self.value() == '3':
            return queryset.filter(
                size__lte=1048576000, size__gt=104857600
            )


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('date_upl', 'date_mod')
    list_display = ('title', 'owner_link', 'sizify')
    # list_display_links = ('title', 'owner')
    list_filter = ('date_upl', PhotoSizeFilter)
    search_fields = (
        'owner__username', 'owner__first_name',
        'owner__last_name', 'owner__email'
    )


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('date_upl', 'date_mod')
    list_display = ('title', 'owner',)
    search_fields = (
        'owner__username', 'owner__first_name',
        'owner__last_name', 'owner__email'
    )


class UserAdmin(admin.ModelAdmin):
    search_fields = (
        'username', 'first_name',
        'last_name', 'email'
    )

admin.site.register(ImagrUser, UserAdmin)
admin.site.register(Relationship)
admin.site.register(Image, ImageAdmin)
admin.site.register(Album, AlbumAdmin)
