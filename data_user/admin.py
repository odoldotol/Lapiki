from django.contrib import admin

from .models import AccountsAsset, AssetsAction, PortfoliosAccount

admin.site.register(PortfoliosAccount)
admin.site.register(AccountsAsset)

@admin.register(AssetsAction)
class AssetsActionAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'asset_buy', 'amount_buy', 'asset_sell', 'amount_sell', 'rabel']