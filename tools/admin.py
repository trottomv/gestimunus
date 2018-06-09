from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Diary

# Register your models here.
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'diarytype', 'customer', 'title', 'text', 'author',)
    search_fields = ('diarytype', 'customer')
    list_filter = ('diarytype', 'customer', 'created_date', 'author',)

admin.site.register(Diary, DiaryAdmin)
