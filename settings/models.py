from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User, Group
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _


# Create your models here.

class CashDesk(models.Model):
	class Meta:
		verbose_name_plural = _("Cash Desks")
		verbose_name = _("Cash Desk")

	u = User.objects.all()
	LIST = ()
	for index, value in enumerate(u):
		singu = (str(index), str(value))
		LIST = LIST + (singu,)

	cashdesk = models.CharField(max_length=200, verbose_name=_('Cash Desk'))
	centercost = models.IntegerField(verbose_name=_('Center Cost'))
	owners = MultiSelectField(choices=LIST, verbose_name=_('Owners'))
	# owners = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	# owners = models.ForeignKey(to=User, null=True, blank=True)

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

    cd = CashDesk.objects.all()
    LIST = ()
    for index, value in enumerate(cd):
        singcd = (str(index+1), str(value))
        LIST = LIST + (singcd,)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    cashdeskowner = MultiSelectField(choices=LIST, null=True, blank=True)

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

	causal = models.CharField(max_length=200)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return u'%s' % (self.causal)

class Operator(models.Model):
	class Meta:
		verbose_name_plural = _("Operators")

    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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
    # class Meta:
    # 	verbose_name_plural = _("Diary Types")

    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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
		verbose_name_plural = _("Service Customers")

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
