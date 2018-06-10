from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import Diary, Agenda

# Register your models here.
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'diaryType', 'customer', 'text', 'created_date', 'sign',)
    search_fields = ('diaryType', 'customer')
    list_filter = ('diaryType', 'customer', 'sign', ('created_date', DateRangeFilter))

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('eventTitle', 'eventStart', 'eventEnd',)


admin.site.register(Diary, DiaryAdmin)
admin.site.register(Agenda, AgendaAdmin)
