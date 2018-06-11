from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import Diary, Agenda

# Register your models here.
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'diaryType', 'customer', 'text', 'created_date', 'sign',)
    search_fields = ('diaryType', 'customer')
    list_filter = ('diaryType', 'customer', 'sign', ('created_date', DateRangeFilter))

class AgendaAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.min.css',
            'https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.print.css',
            'js/fullcalendar.js',
        )
    list_display = ('eventTitle', 'eventCustomer', 'eventDescription', 'eventStart', 'eventEnd',)
    search_fields = ('eventTitle', 'eventCustomer', 'eventDescription')
    list_filter = ('eventTitle', 'eventCustomer', ('eventStart', DateTimeRangeFilter))



admin.site.register(Diary, DiaryAdmin)
admin.site.register(Agenda, AgendaAdmin)
