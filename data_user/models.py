from django.db import models

from data_support.models import AssetFormat
from portfolios.models import Portfolio


class PortfoliosAccount(models.Model):
    # 특정 Portfolio 종속
    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.PROTECT)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 최근 엑세시 일시
    last_access = models.DateTimeField(auto_now=True)
    # 필터
    a = models.BooleanField(default=False, help_text="stocks, etf,,, exchange traded financial instruments")
    b = models.BooleanField(default=False, help_text="crypto")
    c = models.BooleanField(default=False, help_text="cash")
    s = models.BooleanField(default=False, help_text="savings")
    p = models.BooleanField(default=False, help_text="pension, retire, insurance, annuity,,,")
    r = models.BooleanField(default=False, help_text="real estate")
    z = models.BooleanField(default=False, help_text="painting, goods etc")
    # 서버가 정해주는 이름
    title = models.CharField(max_length=30, default="")
    # account 오리지널 이름
    name = models.CharField(max_length=100)
    # 유저가 설정한 이름
    nickname = models.CharField(max_length=50)
    # 유저가 기입한 주석
    remark = models.TextField()


# !!! 이 모델은 절대로 유저가 직접 접근할 수 없어야 합니다 !!!
class AccountsAsset(models.Model):
    # 특정 account 종속
    account = models.ForeignKey(to=PortfoliosAccount, on_delete=models.PROTECT)
    # 포멧 종속
    format = models.ForeignKey(to=AssetFormat, on_delete=models.PROTECT)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 최근 엑세시 일시
    last_access = models.DateTimeField(auto_now=True)
    # asset 코드(특정할 수 있는 고유한 코드)
    code = models.CharField(max_length=50)
    # asset title(대표하는)
    title = models.CharField(max_length=100)
    # asset 이름
    name = models.CharField(max_length=100)
    # asset 속성(필요한 asset에만 사용)
    attribute = models.CharField(max_length=100)
    # asset 수량
    decimal_places = getattr(format, 'amount_decimal_places', 0)
    amount = models.DecimalField(max_digits=100, decimal_places=decimal_places, default=0)
    # portfolio 종속
    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.PROTECT)


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
    action_time = models.DateTimeField(auto_now_add=True)
    # buy/sell asset 종속
    asset_buy = models.ForeignKey(to=AccountsAsset, null=True, on_delete=models.PROTECT, related_name='action_asset_buy')
    asset_sell = models.ForeignKey(to=AccountsAsset, null=True, on_delete=models.PROTECT, related_name='action_asset_sell')
    # buy/sell 수량
    decimal_places_buy = getattr(asset_buy, 'decimal_places', 0)
    decimal_places_sell = getattr(asset_sell, 'decimal_places', 0)
    amount_buy = models.DecimalField(max_digits=100, default=0, decimal_places=decimal_places_buy)
    amount_sell = models.DecimalField(max_digits=100, default=0, decimal_places=decimal_places_sell)
    # 라벨링
    rabel = models.CharField(
        max_length=2,
        choices=action_rabels,
        default=DEFAULT,
    )
    # 특정 account 종속
    account_buy = models.ForeignKey(to=PortfoliosAccount, null=True, on_delete=models.PROTECT, related_name='action_account_buy')
    account_sell = models.ForeignKey(to=PortfoliosAccount, null=True, on_delete=models.PROTECT, related_name='action_account_sell')
    # portfolio 종속
    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.PROTECT)