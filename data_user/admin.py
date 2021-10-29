from django.contrib import admin

from .models import AccountsAsset, AssetsAction, PortfoliosAccount

admin.site.register(PortfoliosAccount)
admin.site.register(AccountsAsset)
admin.site.register(AssetsAction)