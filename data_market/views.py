from django.shortcuts import render, get_object_or_404

from .models import CryptoUSD, TickerSymbol, ExchangeRate

import yfinance as yf


def data_exchangerate(symbol):
    ## symbol 로 환율 데이터 찾아서 있으면 트루 없으면 만들어서 트루 못만들면 폴스
    symbol = symbol.upper()
    exchange = ExchangeRate.objects.filter(symbol=symbol)
    if len(exchange) == 1:
        return True
    elif len(exchange) == 0:
    # 존재하는 symbol이라 가정하고 진행 (symbol ex> KRW=X)
        try:
            # symbol모델로 데이터만들기
            ticker_check = yf.Ticker(symbol)
            info_check = ticker_check.info
            ExchangeRate.objects.create(
                symbol=info_check['symbol'],
                shortName=info_check['shortName'],
                currency=info_check['currency'],
                regularMarketPrice=info_check['regularMarketPrice'],
                previousClose=info_check['previousClose'],
                regularMarketPreviousClose=info_check['regularMarketPreviousClose']
            )
        # 만약에 오류뜨면
        except:
            return False
    return True


def update_exchangerate(symbol):
    try:
        ticker_check = yf.Ticker(symbol)
        info_check = ticker_check.info
        exchange = ExchangeRate.objects.get(symbol=symbol)
        # exchange.symbol=info_check['symbol']
        # exchange.shortName=info_check['shortName']
        # exchange.currency=info_check['currency']
        exchange.regularMarketPrice=info_check['regularMarketPrice']
        exchange.previousClose=info_check['previousClose']
        exchange.regularMarketPreviousClose=info_check['regularMarketPreviousClose']
        exchange.save()
    # 만약에 오류뜨면
    except:
        return False
    return True


def data_tickersymbol(ticker):
    ## ticker 로 심볼 데이터 찾아서 있으면 트루 없으면 만들어서 트루 못만들면 폴스
    ticker = ticker.lower()
    symbol = TickerSymbol.objects.filter(ticker=ticker)
    if len(symbol) == 1:
        return True
    elif len(symbol) == 0:
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


def data_cryptousd(ticker):
    ## ticker 로 심볼 데이터 찾아서 있으면 트루 없으면 만들어서 트루 못만들면 폴스
    ticker.lower()
    symbol = CryptoUSD.objects.filter(ticker=ticker)
    if len(symbol) == 1:
        return True
    elif len(symbol) == 0:
    # 존재하는 symbol이라 가정하고 진행
        try:
            # symbol모델로 데이터만들기
            ticker_check = yf.Ticker(ticker)
            info_check = ticker_check.info
            CryptoUSD.objects.create(
                ticker=ticker,
                symbol=info_check['symbol'],
                name=info_check['name'],
                shortName=info_check['shortName'],
                fromCurrency=info_check['fromCurrency'],
                toCurrency=info_check['toCurrency'],
                currency=info_check['currency'],
                marketCap=info_check['marketCap'],
                regularMarketPrice=info_check['regularMarketPrice'],
                previousClose=info_check['previousClose'],
                regularMarketPreviousClose=info_check['regularMarketPreviousClose'],
            )
        # 만약에 오류뜨면
        except:
            return False
    return True


def update_cryptousd(ticker):
    try:
        ticker_check = yf.Ticker(ticker)
        info_check = ticker_check.info
        cryptousd = CryptoUSD.objects.get(ticker=ticker)
        # cryptousd.symbol=info_check['symbol'],
        # cryptousd.name=info_check['name'],
        # cryptousd.shortName=info_check['shortName'],
        # cryptousd.fromCurrency=info_check['fromCurrency'],
        # cryptousd.toCurrency=info_check['toCurrency'],
        # cryptousd.currency=info_check['currency'],
        cryptousd.marketCap=info_check['marketCap'],
        cryptousd.regularMarketPrice=info_check['regularMarketPrice'],
        cryptousd.previousClose=info_check['previousClose'],
        cryptousd.regularMarketPreviousClose=info_check['regularMarketPreviousClose'],
        cryptousd.save()
    # 만약에 오류뜨면
    except:
        return False
    return True



def update_tickersymbol(ticker):
    try:
        ticker_check = yf.Ticker(ticker)
        info_check = ticker_check.info
        tickersymbol = TickerSymbol.objects.get(ticker=ticker)
        # tickersymbol.symbol=info_check['symbol']
        tickersymbol.shortName=info_check['shortName']
        tickersymbol.longName=info_check['longName']
        # tickersymbol.currency=info_check['currency']
        # tickersymbol.financialCurrency=info_check['financialCurrency']
        tickersymbol.country=info_check['country']
        # tickersymbol.market=info_check['market']
        # tickersymbol.exchange=info_check['exchange']
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
        print(history_check)
        print(history_check['Close'].values[0])
        history_check['Close'].values[0]
    except:
        return False
    return True


def update(request):
    tickersymbols = TickerSymbol.objects.all()
    cryptousds = CryptoUSD.objects.all()
    exchangerates = ExchangeRate.objects.all()
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
    elif request.method == "POST" and request.POST['option'] == "c":
        ticker = request.POST['ticker']
        is_update = data_exchangerate(ticker)
        if is_update == True:
            context = {'result' : '성공'}
        else:
            context = {'result' : '실패'}
        return render(request, 'data_market/update.html', context)
    elif request.method == "POST" and request.POST['option'] == "d":
        for tickersymbol in tickersymbols:
            ticker = tickersymbol.ticker
            is_update = update_tickersymbol(ticker)
            if is_update == False:
                break
        if is_update == False:
            context = {'result' : '실패'}
        context = {'result' : '성공'}
        return render(request, 'data_market/update.html', context)
    elif request.method == "POST" and request.POST['option'] == "e":
        for cryptousd in cryptousds:
            ticker = cryptousd.ticker
            is_update = update_cryptousd(ticker)
            if is_update == False:
                break
        if is_update == False:
            context = {'result' : '실패'}
        context = {'result' : '성공'}
        return render(request, 'data_market/update.html', context)
    elif request.method == "POST" and request.POST['option'] == "f":
        for exchangerate in exchangerates:
            ticker = exchangerate.symbol
            is_update = update_exchangerate(ticker)
            if is_update == False:
                break
        if is_update == False:
            context = {'result' : '실패'}
        context = {'result' : '성공'}
        return render(request, 'data_market/update.html', context)
    else:
        return render(request, 'data_market/update.html')