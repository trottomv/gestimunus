from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.contrib.admin import DateFieldListFilter
from .models import Diary, Agenda, Planner, CashMovements, CashMovementsCustomerDetails, PharmaceuticalInventoryMovements, CashSummary
from settings.models import MovementsCausal, CashDesk, Profile, Customer, OperatorNew
import ast
from datetime import datetime
import json
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from django.db.models import Sum, Count

# Register your models here.

def set_recived(modeladmin, request, queryset):
    for movements in queryset:
        movements.recived = True
        movements.save()
set_recived.short_description = 'Set as "Recived"'

class DiaryAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id'))
        if not request.user.is_superuser:
            qs = super(DiaryAdmin, self).get_queryset(request)
            return qs.filter(services__in=current_user_cashdesk)
        else:
            qs = super(DiaryAdmin, self).get_queryset(request)
            return qs

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id'))

        if db_field.name == "services":
            if not request.user.is_superuser:
                kwargs["queryset"] = CashDesk.objects.filter(
                    id__in=Profile.cashdeskowner.through.objects.filter(
                    profile_id=current_user_profile
                    ).values('cashdesk_id')
                )

        if db_field.name == "customer":
            if not request.user.is_superuser:
                kwargs["queryset"] = Customer.objects.filter(
                    id__in=Customer.services.through.objects.filter(
                    cashdesk_id__in=current_user_cashdesk
                    ).values('customer_id')
                )

        if db_field.name == "sign":
            if not request.user.is_superuser:
                kwargs["queryset"] = OperatorNew.objects.filter(
                    id__in=OperatorNew.services.through.objects.filter(
                    cashdesk_id__in=current_user_cashdesk
                    ).values('operatornew_id')
                )

        return super(DiaryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


    list_display = ('title', 'diaryType', 'services', 'customer', '_text', 'created_date', 'sign', 'upload', 'author')
    search_fields = ('diaryType', 'customer')
    list_filter = (('services', RelatedOnlyFieldListFilter), 'diaryType', ('customer', RelatedOnlyFieldListFilter), ('sign', RelatedOnlyFieldListFilter), ('created_date', DateRangeFilter))

    def _text(self, obj):
        return u'<html>%s</html>' % obj.text
    _text.allow_tags = True

class AgendaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id'))

        if db_field.name == "eventCustomer":
            if not request.user.is_superuser:
                kwargs["queryset"] = Customer.objects.filter(
                    id__in=Customer.services.through.objects.filter(
                    cashdesk_id__in=current_user_cashdesk
                    ).values('customer_id')
                )

        return super(AgendaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('eventTitle', 'eventCustomer', 'eventDescription', 'eventStart', 'eventEnd',)
    search_fields = ('eventTitle', 'eventCustomer', 'eventDescription')
    list_filter = ('eventTitle', 'eventCustomer', ('eventStart', DateTimeRangeFilter))

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):

    change_list_template = 'admin/agenda_scheduler_change_list.html'

    def get_actions(self, request):
        actions = []

class CashMovementsAdminInline(admin.TabularInline):
    model = CashMovementsCustomerDetails
    can_delete = False
    verbose_name_plural = 'Customer Details'
    extra = 0
    class Media:
        js = (
            'js/clonesupplier.js',
        )
    def get_extra (self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id'))

        if db_field.name == "customer":
            if not request.user.is_superuser:
                kwargs["queryset"] = Customer.objects.filter(
                    id__in=Customer.services.through.objects.filter(
                    cashdesk_id__in=current_user_cashdesk
                    ).values('customer_id')
                )

        if db_field.name == "cashdesk":
            if not request.user.is_superuser:
                kwargs["queryset"] = CashDesk.objects.filter(
                    id__in=Profile.cashdeskowner.through.objects.filter(
                    profile_id=current_user_profile
                    ).values('cashdesk_id')
                )


        return super(CashMovementsAdminInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        try:
            cmqs = CashMovements.objects.filter(protocol=obj.protocol)[0].recived
        except:
            pass

        if request.user.is_superuser:
            pass
        else:
            try:
                if cmqs == True:
                    return self.readonly_fields + ('cashdesk', 'customer', 'supplier', 'amount', 'note')
            except:
                pass
        return self.readonly_fields


class CashMovementsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id'))
        qs = super(CashMovementsAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(cashdesk__in=current_user_cashdesk)
        else:
            return qs

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset.model == CashMovements:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.author = request.user
                instance.save()
        else:
            formset.save()

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('recived') #here!

        return super(CashMovementsAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id'))

        if db_field.name == "causal":
            if not request.user.is_superuser:
                kwargs["queryset"] = MovementsCausal.objects.filter(admin=False)

        if db_field.name == "cashdesk":
            if not request.user.is_superuser:
                kwargs["queryset"] = CashDesk.objects.filter(
                    id__in=Profile.cashdeskowner.through.objects.filter(
                    profile_id=current_user_profile
                    ).values('cashdesk_id')
                )

        if db_field.name == "sign":
            if not request.user.is_superuser:
                kwargs["queryset"] = OperatorNew.objects.filter(
                    id__in=OperatorNew.services.through.objects.filter(
                    cashdesk_id__in=current_user_cashdesk
                    ).values('operatornew_id')
                )

        return super(CashMovementsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('protocol', 'operation_date', 'annulled', 'supplier', 'amount', 'cashdesk', 'causal', 'note', 'recived', 'sign', 'author',)
    list_filter = (('causal', RelatedOnlyFieldListFilter), ('cashdesk', RelatedOnlyFieldListFilter), 'recived', ('operation_date', DateRangeFilter))
    inlines = [CashMovementsAdminInline, ]
    actions = [set_recived, ]
    # admin.site.disable_action('delete_selected')
    def get_actions(self, request):
        actions = super(CashMovementsAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            if 'set_recived' in actions:
                del actions['set_recived']
            # if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            pass
        else:
            try:
                if obj.recived == True:
                    return self.readonly_fields + ('recived', 'annulled', 'operation_date', 'document_date', 'cashdesk', 'causal', 'mv_type', 'supplier', 'amount', 'note', 'sign')
            except:
                pass
        return self.readonly_fields


class CashMovementsCustomerDetailsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id'))
        qs = super(CashMovementsCustomerDetailsAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(cashdesk__in=current_user_cashdesk)
        else:
            return qs

    def has_add_permission(self, request):
        return False

    list_display = ('show_prot', 'operation_date', 'cashdesk', 'customer', 'supplier', 'amount', 'note',)
    list_filter = (('customer' , RelatedOnlyFieldListFilter), ('operation_date', DateRangeFilter))
    readonly_fields = ('prot', 'operation_date', 'customer', 'supplier', 'amount', 'note')

    def show_prot(self, obj):
        return '<a href="/tools/cashmovements/%s">%s</a>' % (obj.prot_id, obj.prot)
    show_prot.allow_tags = True

@admin.register(CashSummary)
class CashSummaryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        actions = []

    change_list_template = 'admin/cash_summary_change_list.html'

    def get_queryset(self, request):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id')) #.values('cashdesk')
        if not request.user.is_superuser:
            qse = super(CashSummaryAdmin, self).get_queryset(request)
            return qse.filter(cashdesk__in=current_user_cashdesk)
        else:
            qse = super(CashSummaryAdmin, self).get_queryset(request)
            return qse

    def changelist_view(self, request, extra_context=None):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id')) #.values('cashdesk')
        entry = MovementsCausal.objects.filter(in_out=1)
        exit = MovementsCausal.objects.filter(in_out=2)
        response = super(CashSummaryAdmin, self).changelist_view(request, extra_context)

        try:
            qs = response.context_data['cl'].queryset #.filter(causal_id=exit)
        except (AttributeError, KeyError):
            return response

        metrics = {
            "sum": Sum('amount'),
            "count": Count('cashdesk'),
        }

        response.context_data['summary'] = list(
        qs
        )

        response.context_data['summary_cd'] = list(
        qs
        .values('cashdesk__id', 'cashdesk__cashdesk', 'cashdesk__opening_amount', 'cashdesk__centercost', 'causal_id__in_out').distinct().order_by('cashdesk__centercost').annotate(**metrics) #.filter(cashdesk__in=current_user_cashdesk)
        )

        # response.context_data['summary_causal_entry'] = list(
        # qs.values('causal_id__in_out', 'cashdesk__cashdesk').filter(causal_id__in_out=1).distinct().order_by('cashdesk').annotate(**metrics)
        # )
        #
        # response.context_data['summary_causal_exit'] = list(
        # qs.values('causal_id__in_out', 'causal_id__cashpaymant', 'cashdesk__cashdesk').filter(causal_id__in_out=2).distinct().order_by('cashdesk').annotate(**metrics)
        # )
        #
        # response.context_data['summary_exit'] = list(
        # qs.filter(causal_id__in=exit).values('cashdesk__id').distinct().order_by('cashdesk').annotate(**metrics)
        # )
        #
        # response.context_data['summary_entry'] = list(
        # qs.filter(causal_id__in=entry).values('cashdesk__id').distinct().order_by('cashdesk').annotate(**metrics)
        # )

        return response

    list_filter = (('cashdesk', RelatedOnlyFieldListFilter), ('operation_date', DateRangeFilter))

class PharmaceuticalInventoryMovementsAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values_list('cashdesk_id'))

        if not request.user.is_superuser:
            qs = super(PharmaceuticalInventoryMovementsAdmin, self).get_queryset(request)
            return qs.filter(cashdesk__in=current_user_cashdesk)
        else:
            qs = super(PharmaceuticalInventoryMovementsAdmin, self).get_queryset(request)
            return qs

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        current_user = request.user
        current_user_profile = Profile.objects.filter(user_id=current_user.id)
        current_user_cashdesk = CashDesk.objects.filter(id__in=Profile.cashdeskowner.through.objects.filter(profile_id=current_user_profile).values('cashdesk_id'))

        if db_field.name == "cashdesk":
            if not request.user.is_superuser:
                kwargs["queryset"] = CashDesk.objects.filter(
                    id__in=Profile.cashdeskowner.through.objects.filter(
                    profile_id=current_user_profile
                    ).values('cashdesk_id')
                )

        if db_field.name == "customer":
            if not request.user.is_superuser:
                kwargs["queryset"] = Customer.objects.filter(
                    id__in=Customer.services.through.objects.filter(
                    cashdesk_id__in=current_user_cashdesk
                    ).values('customer_id')
                )

        if db_field.name == "sign":
            if not request.user.is_superuser:
                kwargs["queryset"] = OperatorNew.objects.filter(
                    id__in=OperatorNew.services.through.objects.filter(
                    cashdesk_id__in=current_user_cashdesk
                    ).values('operatornew_id')
                )

        return super(PharmaceuticalInventoryMovementsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('operation_date', 'load_discharge', 'annulled', 'cashdesk', 'customer', 'drug', 'quantity', 'note', 'sign', 'author')
    list_filter = (('customer', RelatedOnlyFieldListFilter), ('cashdesk', RelatedOnlyFieldListFilter), ('operation_date', DateRangeFilter))
    def get_actions(self, request):
        actions = super(PharmaceuticalInventoryMovementsAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            del actions['delete_selected']
            return actions

admin.site.register(Diary, DiaryAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(CashMovements, CashMovementsAdmin)
admin.site.register(CashMovementsCustomerDetails, CashMovementsCustomerDetailsAdmin)
admin.site.register(PharmaceuticalInventoryMovements, PharmaceuticalInventoryMovementsAdmin)
