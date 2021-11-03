from django.contrib import admin

from .models import AssetFormat, FinancialAccountsTitle



admin.site.register(AssetFormat)


@admin.register(FinancialAccountsTitle)
class FinancialAccountsTitleAdmin(admin.ModelAdmin):
    list_display = ['title', 'a', 'b', 'c', 's', 'p']
    list_editable = ['a', 'b', 'c', 's', 'p']