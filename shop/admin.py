from django.contrib import admin
from . import models


admin.site.register(models.Rating)
admin.site.register(models.Size)
admin.site.register(models.Color)
admin.site.register(models.Shop)
admin.site.register(models.Category)
