from django.contrib import admin

from .models import TickerSymbol, ExchangeRate

admin.site.register(TickerSymbol)
admin.site.register(ExchangeRate)