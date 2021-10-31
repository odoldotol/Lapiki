from django.contrib import admin

from .models import AccountsAsset, AssetsAction, PortfoliosAccount, AssetFormat, FinancialAccountsTitle, TickerSymbol

admin.site.register(PortfoliosAccount)
admin.site.register(AccountsAsset)
admin.site.register(AssetsAction)
admin.site.register(AssetFormat)
admin.site.register(TickerSymbol)


@admin.register(FinancialAccountsTitle)
class FinancialAccountsTitleAdmin(admin.ModelAdmin):
    list_display = ['title', 'a', 'b', 'c', 's', 'p']
    list_editable = ['a', 'b', 'c', 's', 'p']