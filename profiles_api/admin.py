from django.contrib import admin
from profiles_api.models import UserProfile,ProfileFeedItem


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields=('email',)


admin.site.register(UserProfile,UserAdmin)
admin.site.register(ProfileFeedItem)
