from django.contrib import admin

# Register your models here.
from .models import Album # Feeding, Toy

# this creates a CRUD for a our cat model in the django admin app
admin.site.register(Album)
# admin.site.register(Second Model)
# admin.site.register(Third Model)