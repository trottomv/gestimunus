from django.contrib import admin
from .models import Operator, Customer, DiariesType, CashDesk, MovementsCausal, Profile, MovementsType
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

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'birthday', 'created_date')
    search_fields = ('surname',)
    list_filter = ('surname',)

class DiariesTypeAdmin(admin.ModelAdmin):
    list_display = ('diarytype', 'created_date')

admin.site.register(Operator, OperatorAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DiariesType, DiariesTypeAdmin)
admin.site.register(CashDesk, CashDeskAdmin)
admin.site.register(MovementsCausal)
admin.site.register(MovementsType)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.site_header = 'Gesti-Munus'
