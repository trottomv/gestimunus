from django.shortcuts import render
from django.db import models
from datetime import datetime
from .models import Agenda #, CashMovementsCustomerDetails
import ast
import json
from django.http import HttpResponse
import pytz

# Create your views here.
cet = pytz.timezone('CET')
offset = cet.utcoffset(datetime.now())

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

def eventsFeed(request):
    entries = ast.literal_eval(json.dumps([dict(item) for item in Agenda.objects.all().values('eventTitle', 'eventDescription', 'eventStart', 'eventEnd', 'id')], cls=DateTimeEncoder))
    json_list = []
    for entry in entries:
        entry_id = entry['id']
        title = entry['eventTitle']
        start = (datetime.strptime(entry['eventStart'], '%Y-%m-%dT%H:%M:%S+00:00') + offset).isoformat()
        end = (datetime.strptime(entry['eventEnd'], '%Y-%m-%dT%H:%M:%S+00:00') + offset).isoformat()
        description = entry['eventDescription']
        url= ("/tools/agenda/" + str(entry_id))
        allDay = False

        json_entry = { 'id': entry_id, 'title': title, 'description': description, 'start':start, 'end':end, 'allDay':allDay, 'url': url}
        json_list.append(json_entry)

    return HttpResponse(json.dumps(json_list), content_type='application/json')

# def supplier(request):
#     supplier = request.POST.get("id_supplier")
