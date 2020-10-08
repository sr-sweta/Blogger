from django.contrib import admin
from .models import Post, BlogComment

# Register your models here.
#admin.site.register(Post)
#admin.site.register(BlogComment)  BELOW format is tuple 
admin.site.register((Post, BlogComment))