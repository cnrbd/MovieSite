from django.contrib import admin

# Register your models here.
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

admin.site.register(Review)
admin.site.register(Movie, MovieAdmin)