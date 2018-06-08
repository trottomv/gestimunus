from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class Operator(models.Model):
	# author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural = "Operatori"

	# sign_id = models.AutoField(primary_key=True)
	name = models.CharField(primary_key=True, max_length=200)
	surname = models.CharField(max_length=200)
	qualify = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s %s' % (self.surname, self.name)


class DiariesType(models.Model):
	# author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural = "Tipi Diario"

	# sign_id = models.AutoField(primary_key=True)
	diarytype = models.CharField(primary_key=True, max_length=200)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.diarytype)


class Customer(models.Model):

	class Meta:
		verbose_name_plural = "Utenti servizio"

	# custid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	birthday = models.DateField()
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s %s' % (self.surname, self.name)
