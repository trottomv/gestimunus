from django.shortcuts import render
from django.db import models
from datetime import datetime
from .models import Agenda
import ast
import json
from django.http import HttpResponse

# Create your views here.
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


def eventsFeed(request):
    from django.utils.timezone import utc
    from django.core.serializers.json import DjangoJSONEncoder

    if request.is_ajax():
        print 'Its ajax from fullCalendar()'

    try:
        start = datetime.fromtimestamp(int(request.GET.get('start', False))).replace(tzinfo=utc)
        end = datetime.fromtimestamp(int(request.GET.get('end',False)))
    except ValueError:
        start = datetime.now.replace(tzinfo=utc)
        end = start + timedelta(days=7)

    # entries = Agenda.objects.filter(date__gte=start).filter(date__lte=end)
    # entries = Agenda.objects.all()
    entries = ast.literal_eval(json.dumps([dict(item) for item in Agenda.objects.all().values('eventTitle', 'eventDescription', 'eventStart', 'eventEnd')], cls=DateTimeEncoder))
    json_list = []
    for entry in entries:
        # entry_id = entry.id
        title = entry['eventTitle']
        start = entry['eventStart']
        end = entry['eventEnd']
        description = entry['eventDescription']
        allDay = False

        json_entry = {'title': title, 'description': description, 'start':start, 'end':end, 'allDay':allDay, }
        json_list.append(json_entry)

    return HttpResponse(json.dumps(json_list), content_type='application/json')
