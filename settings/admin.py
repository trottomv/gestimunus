from django.contrib import admin
from .models import Operator, OperatorNew, Customer, DiariesType, CashDesk, MovementsCausal, Profile, MovementsType, CashPayment
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class CashDeskAdmin(admin.ModelAdmin):
    list_display = ('centercost', 'cashdesk',)
    search_fields = ('centercost', 'cashdesk')
    list_filter = ('cashdesk',)

class OperatorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'qualify', 'created_date')
    search_fields = ('name', 'surname')
    list_filter = ('surname', 'qualify',)

class OperatorNewAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'qualify', 'created_date')
    search_fields = ('name', 'surname')
    list_filter = ('surname', 'qualify',)

class CustomerAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id'))
        if not request.user.is_superuser:
            qs = super(CustomerAdmin, self).get_queryset(request)
            return qs.filter(services__in=current_user_cashdesk)
        else:
            qs = super(CustomerAdmin, self).get_queryset(request)
            return qs


    list_display = ('surname', 'name', 'get_services', 'birthday', 'created_date')
    search_fields = ('surname',)
    list_filter = ('surname', 'services', )

    def get_services(self, obj):
        return ", ".join([p.cashdesk for p in obj.services.all()])

class DiariesTypeAdmin(admin.ModelAdmin):
    list_display = ('diarytype', 'created_date')

class CashPaymentAdmin(admin.ModelAdmin):
    list_display = ('cashpayment', )

# admin.site.register(Operator, OperatorAdmin)
admin.site.register(OperatorNew, OperatorNewAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DiariesType, DiariesTypeAdmin)
admin.site.register(CashDesk, CashDeskAdmin)
admin.site.register(MovementsCausal)
admin.site.register(MovementsType)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(CashPayment, CashPaymentAdmin)
admin.site.site_header = 'Gesti-Munus'
