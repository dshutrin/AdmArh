from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	search_fields = ('pub_date', 'title', 'author')
	list_display = ('pub_date', 'title', 'author')
