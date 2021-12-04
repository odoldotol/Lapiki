from django.db import models

class TickerSymbol(models.Model):
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    symbol = models.CharField(max_length=50, unique=True)

    quoteType = models.CharField(max_length=50, null=True)
    legalType = models.CharField(max_length=50, null=True)

    shortName = models.CharField(max_length=50, null=True)
    longName = models.CharField(max_length=50, null=True)

    currency = models.CharField(max_length=50, null=True)
    financialCurrency = models.CharField(max_length=50, null=True)

    country = models.CharField(max_length=50, null=True)
    market = models.CharField(max_length=50, null=True)
    exchange = models.CharField(max_length=50, null=True)
    exchangeTimezoneName = models.CharField(max_length=50, null=True)
    exchangeTimezoneShortName = models.CharField(max_length=50, null=True)

    currentPrice = models.CharField(max_length=50, null=True)
    previousClose = models.CharField(max_length=50, null=True)
    regularMarketPrice = models.CharField(max_length=50, null=True)
    regularMarketPreviousClose = models.CharField(max_length=50, null=True)

    marketCap = models.CharField(max_length=50, null=True)
    beta = models.CharField(max_length=50, null=True)
    beta3Year = models.CharField(max_length=50, null=True)
    # yield 가 이미 있어서 _ 로 구분함
    _yield = models.CharField(max_length=50, null=True)
    dividendYield = models.CharField(max_length=50, null=True)
    trailingAnnualDividendYield = models.CharField(max_length=50, null=True)
    fiveYearAvgDividendYield = models.CharField(max_length=50, null=True)
    dividendRate = models.CharField(max_length=50, null=True)
    trailingAnnualDividendRate = models.CharField(max_length=50, null=True)
    lastDividendValue = models.CharField(max_length=50, null=True)

    bookValue = models.CharField(max_length=50, null=True)
    priceToBook = models.CharField(max_length=50, null=True)
    enterpriseValue = models.CharField(max_length=50, null=True)

    trailingPE = models.CharField(max_length=50, null=True)
    forwardPE = models.CharField(max_length=50, null=True)
    trailingEps = models.CharField(max_length=50, null=True)
    forwardEps = models.CharField(max_length=50, null=True)


class ExchangeRate(models.Model):
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # symbol ex) KRW=X
    symbol = models.CharField(max_length=50, null=True, unique=True)
    # shortName ex) USD/KRW
    shortName = models.CharField(max_length=50, null=True)
    # currency ex) KRW
    currency = models.CharField(max_length=50, null=True, unique=True)
    # 서버에서 직접 줘야함 ex> Korean Won
    currency_name = models.CharField(max_length=50, null=True)

    regularMarketPrice = models.CharField(max_length=50, null=True)

    previousClose = models.CharField(max_length=50, null=True)
    regularMarketPreviousClose = models.CharField(max_length=50, null=True)


class CryptoUSD(models.Model):
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # BTC-USD
    symbol = models.CharField(max_length=50, null=True, unique=True)

    # bitcoin
    name = models.CharField(max_length=50, null=True)
    # bitcoin USD
    shortName = models.CharField(max_length=50, null=True)

    # BTC
    fromCurrency = models.CharField(max_length=50, null=True)
    # USD=X
    toCurrency = models.CharField(max_length=50, null=True)
    # USD
    currency = models.CharField(max_length=50, null=True)

    marketCap = models.CharField(max_length=50, null=True)

    regularMarketPrice = models.CharField(max_length=50, null=True)

    previousClose = models.CharField(max_length=50, null=True)
    regularMarketPreviousClose = models.CharField(max_length=50, null=True)