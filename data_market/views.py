from django.shortcuts import render, get_object_or_404

from .models import TickerSymbol

import yfinance as yf



def data_tickersymbol(ticker):
    # 존재하는 symbol이라 가정하고 진행
    try:
        # symbol모델로 데이터만들기
        ticker_check = yf.Ticker(ticker)
        info_check = ticker_check.info
        tickersymbol = TickerSymbol.objects.create(
            ticker=ticker,
            symbol=info_check['symbol'],
            shortName=info_check['shortName'],
            longName=info_check['longName'],
            currency=info_check['currency'],
            financialCurrency=info_check['financialCurrency'],
            country=info_check['country'],
            market=info_check['market'],
            exchange=info_check['exchange'],
            marketCap=info_check['marketCap'],
            dividendYield=info_check['dividendYield'],
            trailingEps=info_check['trailingEps'],
            beta=info_check['beta'],
            currentPrice=info_check['currentPrice'],
            previousClose=info_check['previousClose'],
            regularMarketPreviousClose=info_check['regularMarketPreviousClose']
        )
        try:
            tickersymbol.trailingPE=info_check['trailingPE']
            tickersymbol.save()
        except:
            pass
    # 만약에 오류뜨면
    except:
        return False
    return True


def update_tickersymbol(ticker):
    try:
        ticker_check = yf.Ticker(ticker)
        info_check = ticker_check.info
        tickersymbol = TickerSymbol.objects.get(ticker=ticker)
        tickersymbol.symbol=info_check['symbol']
        tickersymbol.shortName=info_check['shortName']
        tickersymbol.longName=info_check['longName']
        tickersymbol.currency=info_check['currency']
        tickersymbol.financialCurrency=info_check['financialCurrency']
        tickersymbol.country=info_check['country']
        tickersymbol.market=info_check['market']
        tickersymbol.exchange=info_check['exchange']
        tickersymbol.marketCap=info_check['marketCap']
        tickersymbol.dividendYield=info_check['dividendYield']
        tickersymbol.trailingEps=info_check['trailingEps']
        tickersymbol.beta=info_check['beta']
        tickersymbol.currentPrice=info_check['currentPrice']
        tickersymbol.previousClose=info_check['previousClose']
        tickersymbol.regularMarketPreviousClose=info_check['regularMarketPreviousClose']
        tickersymbol.save()
        try:
            tickersymbol.trailingPE=info_check['trailingPE']
            tickersymbol.save()
        except:
            pass
    # 만약에 오류뜨면
    except:
        return False
    return True

def update_price(ticker):
    try:
        ticker_check = yf.Ticker(ticker)
        history_check = ticker_check.history(period="1d")
    except:
        return False
    return True


def update(request):
    if request.method == "POST" and request.POST['option'] == "a":
        ticker = request.POST['ticker']
        ticker = ticker.lower()
        is_update = update_tickersymbol(ticker)
        if is_update == True:
            context = {'result' : '성공'}
        else:
            context = {'result' : '실패'}
        return render(request, 'data_market/update.html', context)
    elif request.method == "POST" and request.POST['option'] == "b":
        ticker = request.POST['ticker']
        ticker = ticker.lower()
        is_update = update_price(ticker)
        if is_update == True:
            context = {'result' : '성공'}
        else:
            context = {'result' : '실패'}
        return render(request, 'data_market/update.html', context)
    else:
        return render(request, 'data_market/update.html')