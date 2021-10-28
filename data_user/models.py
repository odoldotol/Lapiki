from os import name
from django.db import models

from Untitled.portfolios.models import Portfolio


class PortfoliosAccount(models.Model):

    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.RESTRICT)

    account_code = models.IntegerField()

    name = models.CharField()

    nickname = models.CharField()


class AccountsAsset(models.Model):

    account = models.ForeignKey(to=PortfoliosAccount, on_delete=models.RESTRICT)

    asset_code = models.IntegerField()

    var = models.IntegerField()

    amount = models.DecimalField(max_digits=100, decimal_places=var)



class AssetsAction(models.Model):

    action_code = models.IntegerField()

    asset_buy = models.ForeignKey(to=AccountsAsset, on_delete=models.RESTRICT)
    
    amount_buy = models.DecimalField(max_digits=100, decimal_places=asset_buy.var)

    asset_sell = models.ForeignKey(to=AccountsAsset, on_delete=models.RESTRICT)

    amount_sell = models.DecimalField(max_digits=100, decimal_places=asset_sell.var)

    created_at = models.DateTimeField(auto_now_add=True)
    
    last_called_at = models.DateTimeField(auto_now=True)
    
    action_time = models.DateTimeField()

    action_number = models.IntegerField()
