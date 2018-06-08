from django.contrib import admin
from .models import Operator, Customer, DiariesType, CashDesk, MovementsCausal

# Register your models here.
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
