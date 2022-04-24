from django.contrib import admin

from .models import Post, Group, Comment


admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comment)
