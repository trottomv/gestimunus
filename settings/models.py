from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User, Group
from multiselectfield import MultiSelectField

# Create your models here.
class CashDesk(models.Model):
	# class Meta:
	# 	verbose_name_plural = "Cassa Centro di Costo"

	u = User.objects.all()
	LIST = ()
	for index, value in enumerate(u):
		singu = (str(index), str(value))
		LIST = LIST + (singu,)

	cashdesk = models.CharField(max_length=200)
	centercost = models.IntegerField()
	owners = MultiSelectField(choices=LIST)
	# owners = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	# owners = models.ForeignKey(to=User, null=True, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.cashdesk)

class MovementsCausal(models.Model):
	# class Meta:
	# 	verbose_name_plural = "Causale"

	causal = models.CharField(max_length=200)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.causal)

class Operator(models.Model):
	# author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	# class Meta:
		# verbose_name_plural = "Operatori"

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
	# class Meta:
	# 	verbose_name_plural = "Tipi Diario"

	# sign_id = models.AutoField(primary_key=True)
	diarytype = models.CharField(primary_key=True, max_length=200)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.diarytype)


class Customer(models.Model):

	# class Meta:
		# verbose_name_plural = "Utenti servizio"

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
