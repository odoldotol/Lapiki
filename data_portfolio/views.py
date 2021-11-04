from django.shortcuts import get_object_or_404, redirect, render

import matplotlib.pyplot as plt

import datetime
from config.views import certification

from data_market.models import ExchangeRate, TickerSymbol
from .models import DataPortfolio, DataPortfolioStockthing
from data_user.models import AccountsAsset, AssetsAction
from portfolios.models import Portfolio
from data_support.models import key_currency

def complete_assets(id, datetime):
    try:
        ##### 포트 아이디와 날짜 받으면 포트내의 모든 액션데이터중 그 날짜까지의 데이터만 모두 연산하여 asset 들의 amount 를 수정하기
        portfolio = get_object_or_404(Portfolio, id=id, is_deleted=False)
        ### 포트 안에있는 asset 필터
        assets = AccountsAsset.objects.filter(portfolio=portfolio)
        ### asset 으로 for문 돌려서 buy 연산하고 저장하기
        for asset in assets:
            actions = AssetsAction.objects.filter(portfolio=portfolio, asset_buy=asset, action_time__lte=datetime)
            com_asset_buy = 0
            com_asset_sell = 0
            for action in actions:
                com_asset_buy = com_asset_buy + action.amount_buy
            actions = AssetsAction.objects.filter(portfolio=portfolio, asset_sell=asset, action_time__lte=datetime)
            for action in actions:
                com_asset_sell = com_asset_sell + action.amount_sell
            asset.amount = com_asset_buy - com_asset_sell
            asset.save()
    except:
        return False
    return True

def open(request, id):
    # 증명
    portfolio = get_object_or_404(Portfolio, id=id, is_deleted=False)
    certi = certification(request, portfolio)
    if certi == False:
        return redirect('accounts:logout')
    # com asset
    now = datetime.datetime.now()
    is_com = complete_assets(id, now)
    if is_com == False:
        return redirect('fail')
    ####### data_portfolio(main) 을 수정하기
    dataportfolio = get_object_or_404(DataPortfolio, portfolio=portfolio, is_main=True)
    ##### 클래스가 a 인 asset 만 모아서 stockthing 수정
    assets = AccountsAsset.objects.filter(portfolio = portfolio, classi='a')
    ### 중복없는 code 리스트 만들기
    code_list = []
    for asset in assets:
        code = [asset.code]
        code_list = code_list + code
    code_set = set(code_list)
    code_list = list(code_set)
    ### code 리스트의 코드로 필터링하여 에셋들을 가져와서 amount 갑을 모두 더하여 stockthing 수정하기
    for code in code_list:
        assets = AccountsAsset.objects.filter(portfolio = portfolio, code=code, classi='a')
        ### stockthing 이 없으면 만들어줘야함
        stockthings = DataPortfolioStockthing.objects.filter(dataportfolio=dataportfolio, symbol=code)
        if len(stockthings) == 0:
            tickersymbol = TickerSymbol.objects.get(symbol=code)
            DataPortfolioStockthing.objects.create(
                dataportfolio=dataportfolio,
                symbol=code,
                country=tickersymbol.country,
                currency=tickersymbol.financialCurrency
            )
        ### 다 더해서 stockthing.amount 에 넣고 저장!
        stockthing = get_object_or_404(DataPortfolioStockthing, dataportfolio=dataportfolio, symbol=code)
        stockthing_amount = 0
        for asset in assets:
            stockthing_amount = stockthing_amount + asset.amount
        stockthing.amount = stockthing_amount
        stockthing.save()
    ##### 마켓 데이터와 포트데이터 연산하기
    stockthing_list = DataPortfolioStockthing.objects.filter(dataportfolio=dataportfolio)
    list_chart_data = []
    for stockthing in stockthing_list:
        ticker = stockthing.symbol
        ticker = ticker.lower()
        ### 적용할 환율 찾기
        if stockthing.currency == key_currency:
            exchangerate = 1
        else:
            currency = stockthing.currency
            exchangerate_symbol = key_currency + "/" + currency
            check = ExchangeRate.objects.filter(shortName=exchangerate_symbol)
            if len(check) == 1:
                ex = ExchangeRate.objects.get(shortName=exchangerate_symbol)
                exchangerate = 1 / float(ex.regularMarketPreviousClose)
            elif len(check) == 0:
                exchangerate_symbol = currency + "/" + key_currency
                check = ExchangeRate.objects.filter(shortName=exchangerate_symbol)
                if len(check) == 1:
                    exchangerate = ex.regularMarketPreviousClose
                else:
                    return redirect('no exchange, please report us, then we`ll fix it today')
        tickersymbol = TickerSymbol.objects.get(ticker=ticker)
        value =  stockthing.amount * float(tickersymbol.regularMarketPreviousClose) * exchangerate
        chart_data = [stockthing.symbol, value]
        list_chart_data = list_chart_data + [chart_data]
    ## value 의 내림차순정렬
    list_chart_data.sort(key=lambda x: (-x[1]))
    ##### 연산한 값으로 이미지파일 생성하여 저장하기

    # ratio = [34, 32, 16, 18]
    # labels = ['Apple', 'Banana', 'Melon', 'Grapes']
    # explode = [0.05, 0.05, 0.05, 0.05]

    # plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode)
    # plt.show()