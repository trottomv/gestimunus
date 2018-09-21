from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User, Group
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _


# Create your models here.
class CashPayment(models.Model):
	class Meta:
		verbose_name_plural = _("Cash Payments")
		verbose_name = _("Cash Payments")

	cashpayment =  models.CharField(max_length=200, verbose_name=_('Cash Payment'))

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.cashpayment)

class CashDesk(models.Model):
	class Meta:
		verbose_name_plural = _("Cash Desks")
		verbose_name = _("Cash Desk")

	# u = User.objects.all()
	# LIST = ()
	# for index, value in enumerate(u):
	# 	singu = (str(index), str(value))
	# 	LIST = LIST + (singu,)

	cashdesk = models.CharField(max_length=200, verbose_name=_('Cash Desk'))
	centercost = models.IntegerField(verbose_name=_('Center Cost'))
	opening_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Opening Amount", null=True)
	# owner = models.ManyToManyField(CashDesk, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.cashdesk)


class Profile(models.Model):
    MANAGER = 1
    OPERATOR = 2
    MED_OPERATOR = 3
    ROLE_CHOICES = (
        (MANAGER, 'Manager'),
        (OPERATOR, 'Social Operator'),
        (MED_OPERATOR, 'OSS'),
    )

    user = models.OneToOneField(User) #, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    cashdeskowner = models.ManyToManyField(CashDesk, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class MovementsCausal(models.Model):
	class Meta:
		verbose_name_plural = _("Movements Causals")

	IN = 1
	OUT = 2
	IN_OUT = (
		(IN, 'IN'),
		(OUT, 'OUT'),
	)

	causal = models.CharField(max_length=200)
	admin = models.BooleanField(default=False, help_text='[Select for assign only to admins]', verbose_name="Admin Only", blank=True)
	in_out = models.PositiveSmallIntegerField(choices=IN_OUT, null=True, verbose_name="In / Out")
	cashpaymant = models.ForeignKey("CashPayment", verbose_name=_('Cash Payment'), null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.causal)

class MovementsType(models.Model):
	class Meta:
		verbose_name_plural = _("Movements Types")

	mv_type = models.CharField(max_length=200)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.mv_type)

# class Operator(models.Model):
# 	class Meta:
# 		verbose_name_plural = _("Operators OLD")
#
# 	name = models.CharField(primary_key=True, max_length=200)
# 	surname = models.CharField(max_length=200)
# 	qualify = models.CharField(max_length=200)
# 	created_date = models.DateTimeField(default=timezone.now)
# 	services = models.ManyToManyField(CashDesk, blank=True)
#
# 	def publish(self):
# 		self.published_date = timezone.now()
# 		self.save()
#
# 	def __str__(self):
# 		return u'%s %s' % (self.surname, self.name)

class OperatorNew(models.Model):
	class Meta:
		verbose_name_plural = _("Operators")

	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	qualify = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	services = models.ManyToManyField(CashDesk, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s %s' % (self.surname, self.name)

class DiariesType(models.Model):
    # class Meta:
    # 	verbose_name_plural = _("Diary Types")

	diarytype = models.CharField(primary_key=True, max_length=200)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.diarytype)


class Customer(models.Model):
	class Meta:
		verbose_name_plural = _("Service Customers")

	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	birthday = models.DateField()
	created_date = models.DateTimeField(default=timezone.now)
	services = models.ManyToManyField(CashDesk, blank=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s %s' % (self.surname, self.name)
