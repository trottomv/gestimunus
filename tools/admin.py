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
    change_list_template = 'admin/agenda_scheduler_change_list.html'
    # date_hierarchy = 'eventStart'
    # form_class = Agenda

    def get_context_data(self, **kwargs):
        context = super(CalendarPage, self).get_context_data(**kwargs)
        context['eventlist'] = Agenda.objects.all()
        return context

admin.site.register(Diary, DiaryAdmin)
admin.site.register(Agenda, AgendaAdmin)
