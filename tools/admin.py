from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.contrib.admin import DateFieldListFilter
from .models import Diary, Agenda, Planner, CashMovements, CashMovementsCustomerDetails
# import serialize
import ast
from datetime import datetime
import json

# Register your models here.

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'diaryType', 'customer', '_text', 'created_date', 'sign', 'upload')
    search_fields = ('diaryType', 'customer')
    list_filter = ('diaryType', 'customer', 'sign', ('created_date', DateRangeFilter))

    def _text(self, obj):
        return u'<html>%s</html>' % obj.text
    _text.allow_tags = True

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
            # 'fullcalendar/lib/moment.min.js',
            # 'fullcalendar/fullcalendar.js',
            # 'fullcalendar/locale-all.js',
            # 'admin/bootstrap/css/bootstrap.css'
        )
    change_list_template = 'adminLTE/agenda_scheduler_change_list.html'

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

class CashMovementsAdminInline(admin.TabularInline):
    model = CashMovementsCustomerDetails
    can_delete = False
    verbose_name_plural = 'Customer Details'



class CashMovementsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if not request.user.is_superuser:
            qs = super(CashMovementsAdmin, self).get_queryset(request)
            return qs.filter(author=request.user)
        else:
            qs = super(CashMovementsAdmin, self).get_queryset(request)
            return qs

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset.model == CashMovements:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.author = request.user
                instance.save()
        else:
            formset.save()

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('recived') #here!
        return super(CashMovementsAdmin, self).get_form(request, obj, **kwargs)

    list_display = ('operation_date', 'annulled', 'supplier', 'amount', 'cashdesk', 'causal', 'note', 'protocol', 'recived', 'sign', 'author',)
    list_filter = ('customer', 'causal', 'cashdesk',)
    inlines = [CashMovementsAdminInline, ]

admin.site.register(Diary, DiaryAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(CashMovements, CashMovementsAdmin)
