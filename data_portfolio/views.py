from django.shortcuts import get_object_or_404, redirect, render

from data_market.models import CryptoUSD, ExchangeRate, TickerSymbol
from .models import DataPortfolio, DataPortfolioCash, DataPortfolioCrypto, DataPortfolioSaving, DataPortfolioStockthing
from data_user.models import AccountsAsset, AssetsAction
from portfolios.models import Portfolio
from data_support.models import key_currency

def complete_assets(id, datetime):
    try:
        ##### 포트 아이디와 날짜 받으면 포트내의 모든 액션데이터중 그 날짜까지의 데이터만 모두 연산하여 asset 들의 amount 를 수정하기
        portfolio = get_object_or_404(Portfolio, id=id, is_deleted=False)
        ### 포트 안에있는 asset 필터
        assets = AccountsAsset.objects.filter(portfolio=portfolio)
        ### asset 으로 for문 돌려서 buy,sell 연산하고 저장하기
        for asset in assets:
            com_asset_buy = 0
            com_asset_sell = 0
            actions = AssetsAction.objects.filter(portfolio=portfolio, asset_buy=asset, action_time__lte=datetime)
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

def data_portfolio_main(portfolio):
    try:
        ####### data_portfolio(main) 을 수정하고 리턴
        dataportfolio = get_object_or_404(DataPortfolio, portfolio=portfolio, is_main=True)
####    ##### 클래스가 a 인 asset 만 모아서 stockthing 수정
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
####    ##### 클래스가 b 인 asset 만 모아서 crypto 수정
        assets = AccountsAsset.objects.filter(portfolio = portfolio, classi='b')
        ### 중복없는 code 리스트 만들기
        code_list = []
        for asset in assets:
            code = [asset.code]
            code_list = code_list + code
        code_set = set(code_list)
        code_list = list(code_set)
        ### code 리스트의 코드로 필터링하여 에셋들을 가져와서 amount 갑을 모두 더하여 stockthing 수정하기
        for code in code_list:
            assets = AccountsAsset.objects.filter(portfolio = portfolio, code=code, classi='b')
            ### crypto 가 없으면 만들어줘야함
            cryptos = DataPortfolioCrypto.objects.filter(dataportfolio=dataportfolio, symbol=code)
            if len(cryptos) == 0:
                symbol = code + '-USD'
                cryptousd = CryptoUSD.objects.get(symbol=symbol)
                DataPortfolioCrypto.objects.create(
                    dataportfolio=dataportfolio,
                    symbol=code,
                    name=cryptousd.name,
                )
            ### 다 더해서 crypto.amount 에 넣고 저장!
            crypto = get_object_or_404(DataPortfolioCrypto, dataportfolio=dataportfolio, symbol=code)
            crypto_amount = 0
            for asset in assets:
                crypto_amount = crypto_amount + asset.amount
            crypto.amount = crypto_amount
            crypto.save()
####    ##### 클래스가 c 인 asset 만 모아서 cash 수정
        assets = AccountsAsset.objects.filter(portfolio = portfolio, classi='c')
        ### 중복없는 code 리스트 만들기
        code_list = []
        for asset in assets:
            code = [asset.code]
            code_list = code_list + code
        code_set = set(code_list)
        code_list = list(code_set)
        ### code 리스트의 코드로 필터링하여 에셋들을 가져와서 amount 갑을 모두 더하여 cash 수정하기
        for code in code_list:
            assets = AccountsAsset.objects.filter(portfolio = portfolio, code=code, classi='c')
            ### cash 가 없으면 만들어줘야함
            cashs = DataPortfolioCash.objects.filter(dataportfolio=dataportfolio, symbol=code)
            if len(cashs) == 0:
                DataPortfolioCash.objects.create(
                    dataportfolio=dataportfolio,
                    symbol=code,
                )
            ### 다 더해서 cash.amount 에 넣고 저장!
            cash = get_object_or_404(DataPortfolioCash, dataportfolio=dataportfolio, symbol=code)
            cash_amount = 0
            for asset in assets:
                cash_amount = cash_amount + asset.amount
            cash.amount = cash_amount
            cash.save()
####    ##### 클래스가 d 인 asset 만 모아서 saving 수정
        ### 에셋들을 가져와서 saving 만들기
        assets = AccountsAsset.objects.filter(portfolio = portfolio, classi='d')
        for asset in assets:
            code = asset.code
            name = asset.name
            ### saving 이 없으면 만들어줘야함
            savings = DataPortfolioSaving.objects.filter(dataportfolio=dataportfolio, symbol=code, name=name)
            if len(savings) == 0:
                DataPortfolioSaving.objects.create(
                    dataportfolio=dataportfolio,
                    symbol=code,
                    name=name
                )
            ### cash.amount 에 넣고 저장!
            saving = get_object_or_404(DataPortfolioSaving, dataportfolio=dataportfolio, symbol=code, name=name)
            saving.amount = asset.amount
            saving.save()
    except:
        return False
    return dataportfolio


def com_dataportfolio_market_preclose(dataportfolio):
    try:
####    ##### 마켓 데이터와 stockthing 포트데이터 연산하기
        stockthing_list = DataPortfolioStockthing.objects.filter(dataportfolio=dataportfolio)
        list_chartdata_stockthing = []
        value_stockthing = 0
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
                        return redirect('no exchange, please report us, then we`ll fix it immediately')
            tickersymbol = TickerSymbol.objects.get(ticker=ticker)
            value = stockthing.amount * float(tickersymbol.regularMarketPreviousClose) * exchangerate
            value_stockthing = value_stockthing + value
            chart_data = [stockthing.symbol, value]
            list_chartdata_stockthing = list_chartdata_stockthing + [chart_data]
####    ##### 마켓 데이터와 crypto 포트데이터 연산하기
        crypto_list = DataPortfolioCrypto.objects.filter(dataportfolio=dataportfolio)
        list_chartdata_crypto = []
        value_crypto = 0
        for crypto in crypto_list:
            symbol = crypto.symbol
            symbol = symbol + '-USD'
            cryptousd = CryptoUSD.objects.get(symbol=symbol)
            value = crypto.amount * float(cryptousd.regularMarketPreviousClose)
            value_crypto = value_crypto + value
            chart_data = [crypto.symbol, value]
            list_chartdata_crypto = list_chartdata_crypto + [chart_data]
####    ##### 마켓 데이터와 cash 포트데이터 연산하기
        cash_list = DataPortfolioCash.objects.filter(dataportfolio=dataportfolio)
        list_chartdata_cash = []
        value_cash = 0
        for cash in cash_list:
            symbol = cash.symbol
            ### 적용할 환율 찾기
            if symbol == key_currency:
                exchangerate = 1
            else:
                currency = symbol
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
                        return redirect('no exchange, please report us, then we`ll fix it immediately')
            value = cash.amount * exchangerate
            value_cash = value_cash + value
            chart_data = [cash.symbol, value]
            list_chartdata_cash = list_chartdata_cash + [chart_data]
####    ##### 마켓 데이터와 saving 포트데이터 연산하기
        saving_list = DataPortfolioSaving.objects.filter(dataportfolio=dataportfolio)
        list_chartdata_saving = []
        value_saving = 0
        for saving in saving_list:
            symbol = saving.symbol
            ### 적용할 환율 찾기
            if symbol == key_currency:
                exchangerate = 1
            else:
                currency = symbol
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
                        return redirect('no exchange, please report us, then we`ll fix it immediately')
            value = saving.amount * exchangerate
            value_saving = value_saving + value
            chart_data = [saving.name, value]
            list_chartdata_saving = list_chartdata_saving + [chart_data]
    except:
        return False
    dataportfolio.stockthing = value_stockthing
    dataportfolio.crypto = value_crypto
    dataportfolio.cash = value_cash
    dataportfolio.saving = value_saving
    dataportfolio.save()
    list_list_chartdata = []
    list_list_chartdata = list_list_chartdata + [list_chartdata_stockthing] + [list_chartdata_crypto] + [list_chartdata_cash] + [list_chartdata_saving]
    return list_list_chartdata


def order_chartdata_by_value(list_chart_data):
    try:
        ## value 의 내림차순정렬
        list_chart_data.sort(key=lambda x: (-x[1]))
        ##### 연산한 값으로 차트 재료 반환
        value_list = []
        label_list = []
        for li in list_chart_data:
            label = li[0]
            val = li[1]
            label_list = label_list + [label]
            value_list = value_list + [val]
    except:
        return False
    ordered_chartdata = []
    ordered_chartdata = ordered_chartdata + [value_list] + [label_list]
    return ordered_chartdata