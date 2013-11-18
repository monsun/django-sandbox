from django.contrib import admin
from dogpics.models import Photographer, Album, Picture

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Album)
admin.site.register(Picture)