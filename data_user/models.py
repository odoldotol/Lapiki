from django.db import models

from portfolios.models import Portfolio


class PortfoliosAccount(models.Model):
    # 특정 Portfolio 종속
    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.RESTRICT)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
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

# 실존하는 금융어카운트 타이틀 구축은 마켓에서 가져오기보다는 유저에게 받아서 서버에서 관리한다. 우리 서비스에서는 절대로 중요해지면 안되는 영역, 최소화가 목표인 영역.
class FinancialAccountsTitle(models.Model):
    # account 에 배정해줄 타이틀
    title = models.CharField(max_length=30)
    # 필터
    a = models.BooleanField(default=False, help_text="stocks, etf,,, exchange traded financial instruments")
    b = models.BooleanField(default=False, help_text="crypto")
    c = models.BooleanField(default=False, help_text="cash")
    s = models.BooleanField(default=False, help_text="savings")
    p = models.BooleanField(default=False, help_text="pension, retire, insurance, annuity,,,")

# 서비스가 커져감에 따라서 발전해야하는 모델. 세상의 모든 asset을 분류,단순화해서 이해하는 모델.
class AssetFormat(models.Model):
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 포멧이름
    title = models.CharField(max_length=50)
    # 수량 소숫점 이하 자릿수
    amount_decimal_places = models.IntegerField(default=0)

# !!! 이 모델은 절대로 유저가 직접 접근할 수 없어야 합니다 !!!
class AccountsAsset(models.Model):
    # 특정 account 종속
    account = models.ForeignKey(to=PortfoliosAccount, on_delete=models.RESTRICT)
    # 포멧 종속
    format = models.ForeignKey(to=AssetFormat, on_delete=models.RESTRICT)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # asset 코드(특정할 수 있는 고유한 이름)
    code = models.CharField(max_length=50)
    # asset 이름
    name = models.CharField(max_length=100)
    # asset 속성(필요한 asset에만 사용)
    attribute = models.CharField(max_length=100)
    # asset 수량
    decimal_places = getattr(format, 'amount_decimal_places', 0)
    amount = models.DecimalField(max_digits=100, decimal_places=decimal_places, default=0)


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
    asset_buy = models.ForeignKey(to=AccountsAsset, null=True, on_delete=models.RESTRICT, related_name='action_buy')
    asset_sell = models.ForeignKey(to=AccountsAsset, null=True, on_delete=models.RESTRICT, related_name='action_sell')
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