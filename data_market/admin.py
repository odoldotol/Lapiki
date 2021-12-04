from django.contrib import admin

from .models import TickerSymbol, ExchangeRate

admin.site.register(ExchangeRate)

@admin.register(TickerSymbol)
class TickerSymbolAdmin(admin.ModelAdmin):
    list_display = [
        'created_at',
        'last_modified_at',

        'symbol',

        'quoteType',
        'legalType',

        'shortName',
        'longName',

        'currency',
        'financialCurrency',

        'country',
        'market',
        'exchange',
        'exchangeTimezoneName',
        'exchangeTimezoneShortName',

        'currentPrice',
        'previousClose',
        'regularMarketPrice',
        'regularMarketPreviousClose',

        'marketCap',
        'beta',
        'beta3Year',
        
        '_yield',
        'dividendYield',
        'trailingAnnualDividendYield',
        'fiveYearAvgDividendYield',
        'dividendRate',
        'trailingAnnualDividendRate',
        'lastDividendValue',

        'bookValue',
        'priceToBook',
        'enterpriseValue',

        'trailingPE',
        'forwardPE',
        'trailingEps',
        'forwardEps',
    ]