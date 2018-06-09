from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import Diary

# Register your models here.
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'diarytype', 'customer', 'text', 'created_date', 'author',)
    search_fields = ('diarytype', 'customer')
    list_filter = ('diarytype', 'customer', 'author', ('created_date', DateRangeFilter))

admin.site.register(Diary, DiaryAdmin)
