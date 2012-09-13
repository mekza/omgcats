# django
from django.contrib import admin

# app
from omgcats.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)
