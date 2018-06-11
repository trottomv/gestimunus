from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.utils.translation import gettext as _


# Create your models here.
class Diary(models.Model):
    class Meta:
        verbose_name_plural = _("Diaries")
        verbose_name = _("Diary")

    diaryType = models.ForeignKey('settings.DiariesType', on_delete=models.CASCADE)
    customer = models.ForeignKey('settings.Customer', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    sign = models.ForeignKey('settings.Operator', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # return u'%s' % (self.diary_id)
        return u'%s %s' % (self.title, self.created_date)

class Agenda(models.Model):

    class Meta:
    	verbose_name_plural = _("Agenda")
        verbose_name = _("Agenda")

    eventTitle = models.CharField(max_length=200)
    eventCustomer = models.ForeignKey('settings.Customer', on_delete=models.CASCADE, blank=True, null=True)
    eventDescription = models.TextField(null=True)
    eventStart = models.DateTimeField()
    eventEnd = models.DateTimeField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return u'%s' % (self.id)
        # return u'%s %s' % (self.title, self.created_date)

class AgendaScheduler(Agenda):
    class Meta:
        proxy = True
    	verbose_name_plural = _("Agenda Planner")
        verbose_name = _("Agenda Planner")
