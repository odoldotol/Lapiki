from django.db import models

from portfolios.models import Portfolio


class DataPortfolio(models.Model):
    # 특정 Portfolio 종속
    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.CASCADE)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 최근 엑세시 일시
    last_access = models.DateTimeField(auto_now=True)
    # main
    is_main = models.BooleanField(default=False)


class DataPortfolioStockthing(models.Model):
    # 특정 dataportfolio 종속
    dataportfolio = models.ForeignKey(to=DataPortfolio, on_delete=models.CASCADE)    
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 최근 엑세시 일시
    last_access = models.DateTimeField(auto_now=True)
    # symbol (=asset.code)
    symbol = models.CharField(max_length=50)
    # acmount
    amount = models.FloatField(default=0)
    # country
    country = models.CharField(max_length=50)
    # currency
    currency = models.CharField(max_length=50, default='')