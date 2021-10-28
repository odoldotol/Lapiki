from os import name
from django.db import models

from Untitled.portfolios.models import Portfolio


class PortfoliosAccount(models.Model):

    account_code1 = models.IntegerField()

    account_code2 = models.IntegerField()

    account_code3 = models.IntegerField()

    account_code4 = models.IntegerField()

    name1 = models.CharField()

    name2 = models.CharField()

    name3 = models.CharField()

    nickname = models.CharField()

    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.RESTRICT)


class AccountsAsset(models.Model):

    

    account = models.ForeignKey(to=PortfoliosAccount, on_delete=models.RESTRICT)



class Action(models.Model):

    asset_buy = models.ForeignKey(to=AccountsAsset, on_delete=models.RESTRICT)
    
    amount_buy = models.DecimalField(max_digits=50, decimal_places=2)

    asset_sell = models.ForeignKey(to=AccountsAsset, on_delete=models.RESTRICT)

    amount_sell = models.DecimalField(max_digits=50, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    
    last_called_at = models.DateTimeField(auto_now=True)
    
    action_time = models.DateTimeField()

    action_number = models.IntegerField()
