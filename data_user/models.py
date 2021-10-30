from django.db import models

from portfolios.models import Portfolio, AccountFormat, AssetFormat


class PortfoliosAccount(models.Model):
    # 특정 Portfolio 종속
    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.RESTRICT)
    # 포멧 종속
    format = models.ForeignKey(to=AccountFormat, on_delete=models.RESTRICT)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # account 코드
    code = models.CharField(max_length=50)
    # account 기본이름
    name = models.CharField(max_length=100)
    # 유저가 설정한 이름
    nickname = models.CharField(max_length=50)
    # 유저가 기입한 주석
    remark = models.TextField()


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
    rabel = models.CharField(max_length=100)

