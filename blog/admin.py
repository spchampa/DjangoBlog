from django.contrib import admin
from .models import Post
# Register your models here.

# puts the models into the admin page of the site
admin.site.register(Post)