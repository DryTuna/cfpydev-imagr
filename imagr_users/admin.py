from django.contrib import admin
from imagr_users.models import ImagrUser, Relationship


class UserAdmin(admin.ModelAdmin):
    search_fields = (
        'username', 'first_name',
        'last_name', 'email'
    )
admin.site.register(ImagrUser, UserAdmin)
admin.site.register(Relationship)
