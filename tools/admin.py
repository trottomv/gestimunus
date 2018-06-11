from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import Diary, Agenda, AgendaScheduler

# Register your models here.

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'diaryType', 'customer', 'text', 'created_date', 'sign',)
    search_fields = ('diaryType', 'customer')
    list_filter = ('diaryType', 'customer', 'sign', ('created_date', DateRangeFilter))

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('eventTitle', 'eventCustomer', 'eventDescription', 'eventStart', 'eventEnd',)
    search_fields = ('eventTitle', 'eventCustomer', 'eventDescription')
    list_filter = ('eventTitle', 'eventCustomer', ('eventStart', DateTimeRangeFilter))

@admin.register(AgendaScheduler)
class AgendaSchedulerAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://code.jquery.com/jquery-1.12.4.min.js',
            'https://code.jquery.com/ui/1.12.0/jquery-ui.min.js',
            'https://code.jquery.com/ui/1.12.0/themes/smoothness/jquery-ui.css',
            'https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.min.css',
            'https://cdnjs.cloudflare.com/ajax/libs/fullcalendar/3.9.0/fullcalendar.print.css',
            'js/fullcalendar.js',
        )
    change_list_template = 'admin/agenda_scheduler_change_list.html'
    date_hierarchy = 'eventStart'

admin.site.register(Diary, DiaryAdmin)
admin.site.register(Agenda, AgendaAdmin)
