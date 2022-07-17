from django.contrib import admin

from .models import postModel


class postAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(postModel, postAdmin)
