from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Diaries

# Register your models here.
class DiariesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'diarytype', 'customer', 'title', 'text', 'author',)
    search_fields = ('diarytype', 'customer')
    list_filter = ('diarytype', 'customer', 'created_date', 'author',)

admin.site.register(Diaries, DiariesAdmin)
