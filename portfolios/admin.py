from django.contrib import admin

from .models import Portfolio, AccountFormat, AssetFormat

admin.site.register(Portfolio)
admin.site.register(AccountFormat)
admin.site.register(AssetFormat)
