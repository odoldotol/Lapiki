from django.db import models
from django.conf import settings


# 기준통화 세팅
key_currency = getattr(settings, 'KEY_CURRENCY', "USD")


# 실존하는 금융어카운트 타이틀 구축은 마켓에서 가져오기보다는 유저에게 받아서 서버에서 관리한다. 우리 서비스에서는 절대로 중요해지면 안되는 영역, 최소화가 목표인 영역.
class FinancialAccountsTitle(models.Model):
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
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
    # 포멧코드
    code = models.CharField(max_length=50, default='')
    # 수량 소숫점 이하 자릿수
    amount_decimal_places = models.IntegerField(default=0)