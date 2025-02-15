from django.contrib import admin
from .models import Singer, Song

# Register your models here.

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']

@admin.register(Song)  
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'formatted_duration', 'singer']

    def formatted_duration(self, obj):
        return f'{obj.duration} mins'