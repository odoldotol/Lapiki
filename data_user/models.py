from django.db import models

from portfolios.models import Portfolio


class PortfoliosAccount(models.Model):
    # 특정 Portfolio 종속
    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.RESTRICT)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 
    a = models.BooleanField(default=False, help_text="stocks, etf,,, exchange traded financial instruments")
    b = models.BooleanField(default=False, help_text="crypto")
    c = models.BooleanField(default=False, help_text="cash")
    s = models.BooleanField(default=False, help_text="savings")
    p = models.BooleanField(default=False, help_text="pension, retire, insurance, annuity,,,")
    r = models.BooleanField(default=False, help_text="real estate")
    z = models.BooleanField(default=False, help_text="painting, goods etc")
    #
    title = models.CharField(max_length=30, default="")
    # account 기본이름
    name = models.CharField(max_length=100)
    # 유저가 설정한 이름
    nickname = models.CharField(max_length=50)
    # 유저가 기입한 주석
    remark = models.TextField()


class FinancialAccountsTitle(models.Model):
    #
    title = models.CharField(max_length=30)
    #
    a = models.BooleanField(default=False, help_text="stocks, etf,,, exchange traded financial instruments")
    b = models.BooleanField(default=False, help_text="crypto")
    c = models.BooleanField(default=False, help_text="cash")
    s = models.BooleanField(default=False, help_text="savings")
    p = models.BooleanField(default=False, help_text="pension, retire, insurance, annuity,,,")


class AssetFormat(models.Model):
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 포멧이름
    title = models.CharField(max_length=50)
    # 수량 소숫점 이하 자릿수
    amount_decimal_places = models.IntegerField()


class AccountsAsset(models.Model):
    # 특정 account 종속
    account = models.ForeignKey(to=PortfoliosAccount, on_delete=models.RESTRICT)
    # 포멧 종속
    format = models.ForeignKey(to=AssetFormat, on_delete=models.RESTRICT)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # asset 코드
    code = models.CharField(max_length=50)
    # asset 이름
    name = models.CharField(max_length=100)
    # asset 속성
    attribute = models.CharField(max_length=100)
    # asset 수량
    decimal_places = getattr(format, 'amount_decimal_places', 0)
    amount = models.DecimalField(max_digits=100, decimal_places=decimal_places)


DEFAULT = 'DF'
QUICK = 'QK'
TRADE = 'TD'
INOUT = 'IO'
INSIDE = 'IS'
USER = 'US'
INTEREST = 'IR'
DIVIDEND = 'DD'
RENT = 'RT'
PAY = 'PY'

action_rabels = [
    (DEFAULT, 'default'),
    (QUICK, '빠른생성'),
    (TRADE, '거래'),
    (INOUT, '입출'),
    (INSIDE, '내부거래'),
    (USER, '수정'),
    (INTEREST, '이자'),
    (DIVIDEND, '배당'),
    (RENT, '월세'),
    (PAY, '급여'),
]

class AssetsAction(models.Model):
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 실제 액션 일시
    action_time = models.DateTimeField()
    # buy/sell asset 종속
    asset_buy = models.ForeignKey(to=AccountsAsset, on_delete=models.RESTRICT, related_name='action_buy')
    asset_sell = models.ForeignKey(to=AccountsAsset, on_delete=models.RESTRICT, related_name='action_sell')
    # buy/sell 수량
    decimal_places_buy = getattr(asset_buy, 'decimal_places', 0)
    decimal_places_sell = getattr(asset_sell, 'decimal_places', 0)
    amount_buy = models.DecimalField(max_digits=100, decimal_places=decimal_places_buy)
    amount_sell = models.DecimalField(max_digits=100, decimal_places=decimal_places_sell)
    # 라벨링
    rabel = models.CharField(
        max_length=2,
        choices=action_rabels,
        default=DEFAULT,
    )


class TickerSymbol(models.Model):
    ticker = models.CharField(max_length=50, unique=True)

    symbol = models.CharField(max_length=50, unique=True)

    shortName = models.CharField(max_length=50)
    longName = models.CharField(max_length=50)

    currency = models.CharField(max_length=50)
    financialCurrency = models.CharField(max_length=50)

    country = models.CharField(max_length=50)
    market = models.CharField(max_length=50)
    exchange = models.CharField(max_length=50)

    marketCap = models.CharField(max_length=50)
    trailingPE = models.CharField(max_length=50)
    dividendYield = models.CharField(max_length=50)

    trailingEps = models.CharField(max_length=50)
    beta = models.CharField(max_length=50)

    currentPrice = models.CharField(max_length=50)