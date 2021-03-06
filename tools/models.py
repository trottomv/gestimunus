from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.utils.translation import gettext as _
from tinymce import HTMLField
from gestimunus import settings
from recurrence.fields import RecurrenceField
from settings.models import CashDesk, MovementsCausal, Customer, Profile, DiariesType, OperatorNew
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField

from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver


# Create your models here.

def protocolgen():
	# return 201803001 + CashMovements.objects.count() + 1
	try:
		qs = CashMovements.objects.latest('protocol')
		if str(qs.protocol)[0:6] == timezone.now().strftime("%Y%m"):
			protocol = int(timezone.now().strftime("%Y") + timezone.now().strftime("%m") + format(int(str(qs.protocol)[6:]) + 1, "04"))
			return protocol
		else:
			protocol = int(timezone.now().strftime("%Y") + timezone.now().strftime("%m") + format(1, "04"))
			return protocol
	except:
		protocol = int(timezone.now().strftime("%Y") + timezone.now().strftime("%m") + format(1, "04"))
		return protocol


class Diary(models.Model):
	class Meta:
		verbose_name_plural = _("Diaries")
		verbose_name = _("Diary")

	author = models.ForeignKey(
		User,
		null=True,
		editable=False,
    on_delete=models.CASCADE
	)

	diaryType = models.ForeignKey(DiariesType, on_delete=models.CASCADE, verbose_name="Diary Type")
	services = models.ForeignKey(CashDesk, on_delete=models.CASCADE, null=True, verbose_name="Service")
	# customer = models.ForeignKey('settings.Customer', on_delete=models.CASCADE, blank=True, null=True)
	customer = ChainedForeignKey(
        Customer,
		verbose_name='Customer',
		chained_field="services",
        chained_model_field="services",
		auto_choose = True,
		show_all = False,
		null = True,
		blank= True)
	title = models.CharField(max_length=200)
	text = HTMLField('Content', blank=True)
	upload = models.FileField(upload_to=settings.STATIC_UPLOAD, null=True, blank=True)
	# sign = models.ForeignKey('settings.OperatorNew', on_delete=models.CASCADE, null=True, verbose_name="Service")

	sign = ChainedForeignKey(
		OperatorNew,
		verbose_name="Sign",
		chained_field='services',
		chained_model_field='services',
		null=True)

	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		# return u'%s' % (self.diary_id)
		return u'%s %s' % (self.created_date.strftime("%Y-%m-%d"), self.title, )

class Agenda(models.Model):

	class Meta:
		verbose_name_plural = _("Events")
		verbose_name = _("Event")

	eventTitle = models.CharField(max_length=200, verbose_name="Title")
	eventCustomer = models.ForeignKey('settings.Customer', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Customer")
	eventDescription = models.TextField(null=True, verbose_name="Description")
	eventStart = models.DateTimeField(verbose_name="Start at")
	eventEnd = models.DateTimeField(verbose_name="End at")
	recurrence = RecurrenceField(null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.eventTitle)
	    # return u'%s %s' % (self.title, self.created_date)

class Planner(Agenda):

	class Meta:
		proxy = True
		verbose_name_plural = _("Events Planner")
		verbose_name = _("Agenda")

class CashMovements(models.Model):

	class Meta:
		verbose_name_plural = "Cash Movements"

	author = models.ForeignKey(
		User,
		null=True,
		editable=False,
    on_delete=models.CASCADE
	)

	protocol = models.IntegerField(unique=True, editable=False, default=protocolgen)
	annulled = models.BooleanField(default=True, help_text='[Deselect for cancel entry]', verbose_name="Validation")
	recived = models.NullBooleanField(default=False, verbose_name="Recived")
	operation_date = models.DateField(verbose_name="Operation Date", default=timezone.now)
	document_date =  models.DateField(blank=True, null=True, verbose_name="Document Date")
	cashdesk = models.ForeignKey('settings.CashDesk', verbose_name="Cash Service", on_delete=models.CASCADE)
	causal = models.ForeignKey('settings.MovementsCausal', verbose_name="Causal", on_delete=models.CASCADE)
	mv_type = models.ForeignKey('settings.MovementsType', verbose_name="Type", null=True, blank=True, on_delete=models.CASCADE)
	supplier = models.CharField(max_length=500, verbose_name="Supplier", null=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount", help_text='(Use "." as decimal separator)')
	customer = models.ForeignKey('settings.Customer', null=True, blank=True, editable=False, verbose_name="Service Customer", on_delete=models.CASCADE)
	note = models.CharField(max_length=200, blank=True, verbose_name="Note")
	sign = ChainedForeignKey(
		'settings.OperatorNew',
		verbose_name="Sign",
		chained_field='cashdesk',
		chained_model_field='services',
		null=True,
    on_delete=models.CASCADE
  )


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		# return u'%s %s %s %s' % (self.operation_date, self.amount, self.causal, self.cashdesk)
		return u'%s' % (self.protocol)


class CashMovementsCustomerDetails(models.Model):

	class Meta:
		verbose_name_plural = "Cash Movements Customer Details"

	prot = models.ForeignKey('CashMovements', on_delete=models.CASCADE)
	# cashdesk = models.CharField(max_length=200, verbose_name="cashdesk", null=True, blank=True, editable=False)

	cashdesk = models.ForeignKey(CashDesk, null=True, editable=False, on_delete=models.CASCADE)
	# cashdesk = CashMovements.cashdesk
	operation_date = models.DateField(default=timezone.now, editable=False)
	customer = models.ForeignKey(Customer, null=True, blank=True, verbose_name="Service Customer", on_delete=models.CASCADE)
	# customer = ChainedForeignKey(
    #     'settings.Customer',
	# 	verbose_name='Service Customer',
	# 	chained_field='cashdesk',
    #     chained_model_field='services',
	# 	null=True)
	supplier = models.CharField(max_length=200, verbose_name="Supplier", null=True, blank=True, editable=False)
	amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount", blank=True)
	note = models.CharField(max_length=200, blank=True, verbose_name="Note")

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.prot)


class CashSummary(CashMovements):

	class Meta:
		proxy = True
		verbose_name = 'Cash Summary'
		verbose_name_plural = 'Cash Summary'


class PharmaceuticalInventoryMovements(models.Model):

	class Meta:
		verbose_name_plural = "Pharmaceutical Inventory Movements"
		verbose_name = "Pharma Inventory"

	IN = 1
	OUT = 2
	IN_OUT = (
		(IN, 'LOAD'),
		(OUT, 'UNLOAD'),
	)

	author = models.ForeignKey(
			User,
			null=True,
			editable=False,
      on_delete=models.CASCADE
	)

	load_discharge = models.PositiveSmallIntegerField(choices=IN_OUT, null=True, verbose_name="Load / Discharge")
	annulled = models.BooleanField(default=True, help_text='[Deselect for cancel entry]', verbose_name="Validation")
	operation_date = models.DateField(verbose_name="Operation Date", default=timezone.now)
	cashdesk = models.ForeignKey('settings.CashDesk', verbose_name="Cash Service", on_delete=models.CASCADE)
	customer = ChainedForeignKey(
        'settings.Customer',
		verbose_name='Customer',
		chained_field="cashdesk",
    chained_model_field="services",
		auto_choose = True,
		show_all = False,
		null = True)
	drug = models.CharField(max_length=200, blank=True, verbose_name="Generic Drug")
	quantity = models.IntegerField()
	note = models.CharField(max_length=200, blank=True, verbose_name="Note")
	sign = ChainedForeignKey(
		'settings.OperatorNew',
		 verbose_name="Sign",
		 chained_field='cashdesk',
		 chained_model_field='services')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.id)


@receiver(pre_save, sender=CashMovementsCustomerDetails)
def get_supplier(sender, instance, *args, **kwargs):
	supplier = CashMovements.objects.filter(id=instance.prot_id).values('supplier')[0]['supplier']
	cashdesk = CashMovements.objects.filter(id=instance.prot_id).values('cashdesk_id')[0]['cashdesk_id']
	instance.supplier = supplier
	instance.cashdesk_id = cashdesk
