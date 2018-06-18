from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import Diary, Agenda, Planner
# import serialize
import ast
from datetime import datetime
import json

# Register your models here.

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'diaryType', 'customer', 'text', 'created_date', 'sign',)
    search_fields = ('diaryType', 'customer')
    list_filter = ('diaryType', 'customer', 'sign', ('created_date', DateRangeFilter))

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('eventTitle', 'eventCustomer', 'eventDescription', 'eventStart', 'eventEnd',)
    search_fields = ('eventTitle', 'eventCustomer', 'eventDescription')
    list_filter = ('eventTitle', 'eventCustomer', ('eventStart', DateTimeRangeFilter))

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):
    class Media:
        js = (
            # 'fullcalendar/lib/jquery-ui.min.js',
            # 'fullcalendar/lib/jquery.min.js',
            'fullcalendar/lib/moment.min.js',
            # 'fullcalendar/fullcalendar.js',
            'fullcalendar/locale-all.js',
        )
    change_list_template = 'admin/agenda_scheduler_change_list.html'

    # events = ast.literal_eval(serialize('json', Agenda.objects.all()))
    # events = ast.literal_eval(data)
    # date_hierarchy = 'eventStart'
    # form_class = Agenda

    # def get_context_data(self, **kwargs):
    #     context = super(AgendaAdmin, self).get_context_data(**kwargs)
    #     events = ast.literal_eval(json.dumps([dict(item) for item in Agenda.objects.all().values('eventTitle', 'eventStart', 'eventEnd')], cls=DateTimeEncoder))
    #     for i in events:
    #         import pdb; pdb.set_trace()
    #         context['title'] = i['eventTitle']
    #         context['start'] = i['eventStart']
    #         context['end']  = i['eventEnd']
    #     # context['events'] = ast.literal_eval(json.dumps([dict(item) for item in Agenda.objects.all().values('eventTitle', 'eventStart', 'eventEnd')], cls=DateTimeEncoder))
    #     return context


admin.site.register(Diary, DiaryAdmin)
admin.site.register(Agenda, AgendaAdmin)
