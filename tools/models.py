from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.contrib import admin

# Create your models here.
class Diaries(models.Model):
	class Meta:
		verbose_name_plural = "Diari"

	author = models.ForeignKey('settings.Operator', on_delete=models.CASCADE)
	diarytype = models.ForeignKey('settings.DiariesType', on_delete=models.CASCADE)
	customer = models.ForeignKey('settings.Customer', on_delete=models.CASCADE, blank=True, null=True)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		# return u'%s' % (self.diary_id)
		return u'%s %s' % (self.title, self.created_date)
