from django.contrib import admin
from imagr_users.models import ImagrUser, Relationship
# Register your models here.
admin.site.register(ImagrUser)
admin.site.register(Relationship)
