from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'description')
    list_filter = ('category', )

admin.site.register(product, ProductAdmin)
