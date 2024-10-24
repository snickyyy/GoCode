from django.contrib import admin

from accounts.models import GoUser

# Register your models here.


@admin.register(GoUser)
class GoUserAdmin(admin.ModelAdmin):
    ...
