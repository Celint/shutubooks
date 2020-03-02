from django.contrib import admin
from .models import article,image
# Register your models here.
# class imageIn(admin.TabularInline):
#     model = image
# #     extra = 2
# class articleAdmin(admin.ModelAdmin):
#     inlines = [imageIn]
admin.site.register(article)
admin.site.register(image)

