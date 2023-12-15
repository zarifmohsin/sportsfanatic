from django.contrib import admin

# Register your models here.
from .models import Post, Replies, Profile

admin.site.register(Post)
admin.site.register(Replies)
admin.site.register(Profile)