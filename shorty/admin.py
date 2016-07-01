'''Shorty Admin'''

from .models import ShortURL
from django.contrib import admin


class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('path', 'redirect', 'external', 'user')

admin.site.register(ShortURL, ShortURLAdmin)
