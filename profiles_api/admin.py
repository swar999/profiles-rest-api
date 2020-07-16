from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields=('email',)


admin.site.register(UserProfile,UserAdmin)
