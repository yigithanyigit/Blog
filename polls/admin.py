from django.contrib import admin
from .models import Post




class MyModelAdmin(admin.ModelAdmin):
    list_per_page = 400
    admin.site.register(Post)