from django.db import models

class TickerSymbol(models.Model):
    ticker = models.CharField(max_length=50, unique=True)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_modified_at = models.DateTimeField(auto_now=True, null=True)

    symbol = models.CharField(max_length=50, unique=True)

    shortName = models.CharField(max_length=50, null=True)
    longName = models.CharField(max_length=50, null=True)

    currency = models.CharField(max_length=50, null=True)
    financialCurrency = models.CharField(max_length=50, null=True)

    country = models.CharField(max_length=50, null=True)
    market = models.CharField(max_length=50, null=True)
    exchange = models.CharField(max_length=50, null=True)

    marketCap = models.CharField(max_length=50, null=True)
    trailingPE = models.CharField(max_length=50, null=True)
    dividendYield = models.CharField(max_length=50, null=True)

    trailingEps = models.CharField(max_length=50, null=True)
    beta = models.CharField(max_length=50, null=True)

    currentPrice = models.CharField(max_length=50, null=True)

    previousClose = models.CharField(max_length=50, null=True)
    regularMarketPreviousClose = models.CharField(max_length=50, null=True)