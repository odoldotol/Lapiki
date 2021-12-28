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
    symbol = TickerSymbol.objects.filter(symbol=ticker)
    if len(symbol) == 1:
        return True
    elif len(symbol) == 0:
        # 존재하는 symbol이라 가정하고 진행
        try:
            # symbol모델로 데이터만들기
            ticker_check = yf.Ticker(ticker)
            info_check = ticker_check.info

            try:
                symbol = info_check['symbol']
            except:
                symbol = None
            try:
                quoteType = info_check['quoteType']
            except:
                quoteType = None
            try:
                legalType = info_check['legalType']
            except:
                legalType = None
            try:
                shortName = info_check['shortName']
            except:
                shortName = None
            try:
                longName = info_check['longName']
            except:
                longName = None
            try:
                currency = info_check['currency']
            except:
                currency = None
            try:
                financialCurrency = info_check['financialCurrency']
            except:
                financialCurrency = None
            try:
                country = info_check['country']
            except:
                country = None
            try:
                market = info_check['market']
            except:
                market = None
            try:
                exchange = info_check['exchange']
            except:
                exchange = None
            try:
                exchangeTimezoneName = info_check['exchangeTimezoneName']
            except:
                exchangeTimezoneName = None
            try:
                exchangeTimezoneShortName = info_check['exchangeTimezoneShortName']
            except:
                exchangeTimezoneShortName = None
            try:
                currentPrice = info_check['currentPrice']
            except:
                currentPrice = None
            try:
                previousClose = info_check['previousClose']
            except:
                previousClose = None
            try:
                regularMarketPrice = info_check['regularMarketPrice']
            except:
                regularMarketPrice = None
            try:
                regularMarketPreviousClose = info_check['regularMarketPreviousClose']
            except:
                regularMarketPreviousClose = None
            try:
                marketCap = info_check['marketCap']
            except:
                marketCap = None
            try:
                beta = info_check['beta']
            except:
                beta = None
            try:
                beta3Year = info_check['beta3Year']
            except:
                beta3Year = None
            try:
                _yield = info_check['yield']
            except:
                _yield = None
            try:
                dividendYield = info_check['dividendYield']
            except:
                dividendYield = None
            try:
                trailingAnnualDividendYield = info_check['trailingAnnualDividendYield']
            except:
                trailingAnnualDividendYield = None
            try:
                fiveYearAvgDividendYield = info_check['fiveYearAvgDividendYield']
            except:
                fiveYearAvgDividendYield = None
            try:
                dividendRate = info_check['dividendRate']
            except:
                dividendRate = None
            try:
                trailingAnnualDividendRate = info_check['trailingAnnualDividendRate']
            except:
                trailingAnnualDividendRate = None
            try:
                lastDividendValue = info_check['lastDividendValue']
            except:
                lastDividendValue = None
            try:
                bookValue = info_check['bookValue']
            except:
                bookValue = None
            try:
                priceToBook = info_check['priceToBook']
            except:
                priceToBook = None
            try:
                enterpriseValue = info_check['enterpriseValue']
            except:
                enterpriseValue = None
            try:
                trailingPE = info_check['trailingPE']
            except:
                trailingPE = None
            try:
                forwardPE = info_check['forwardPE']
            except:
                forwardPE = None
            try:
                trailingEps = info_check['trailingEps']
            except:
                trailingEps = None
            try:
                forwardEps = info_check['forwardEps']
            except:
                forwardEps = None

            if quoteType != "ETF" and quoteType != "EQUITY":
                return False

            TickerSymbol.objects.create(
                symbol=symbol,
                quoteType=quoteType,
                legalType=legalType,
                shortName=shortName,
                longName=longName,
                currency=currency,
                financialCurrency=financialCurrency,
                country=country,
                market=market,
                exchange=exchange,
                exchangeTimezoneName=exchangeTimezoneName,
                exchangeTimezoneShortName=exchangeTimezoneShortName,
                currentPrice=currentPrice,
                previousClose=previousClose,
                regularMarketPrice=regularMarketPrice,
                regularMarketPreviousClose=regularMarketPreviousClose,
                marketCap=marketCap,
                beta=beta,
                beta3Year=beta3Year,
                _yield=_yield,
                dividendYield=dividendYield,
                trailingAnnualDividendYield=trailingAnnualDividendYield,
                fiveYearAvgDividendYield=fiveYearAvgDividendYield,
                dividendRate=dividendRate,
                trailingAnnualDividendRate=trailingAnnualDividendRate,
                lastDividendValue=lastDividendValue,
                bookValue=bookValue,
                priceToBook=priceToBook,
                enterpriseValue=enterpriseValue,
                trailingPE=trailingPE,
                forwardPE=forwardPE,
                trailingEps=trailingEps,
                forwardEps=forwardEps
            )
        # 만약에 오류뜨면
        except:
            return False
    return True


def data_cryptousd(ticker):
    ## ticker 로 심볼 데이터 찾아서 있으면 트루 없으면 만들어서 트루 못만들면 폴스
    symbol = CryptoUSD.objects.filter(symbol=ticker)
    if len(symbol) == 1:
        return True
    elif len(symbol) == 0:
    # 존재하는 symbol이라 가정하고 진행
        try:
            # symbol모델로 데이터만들기
            ticker_check = yf.Ticker(ticker)
            info_check = ticker_check.info

            quoteType = info_check['quoteType']
            if quoteType != "CRYPTOCURRENCY":
                return False
                
            try:
                name = info_check['name']
            except:
                name = None
                
            CryptoUSD.objects.create(
                symbol=info_check['symbol'],
                name=name,
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
        cryptousd = CryptoUSD.objects.get(symbol=ticker)
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
        tickersymbol = TickerSymbol.objects.get(symbol=ticker)

        try:
            symbol = info_check['symbol']
        except:
            symbol = None
        try:
            quoteType = info_check['quoteType']
        except:
            quoteType = None
        try:
            legalType = info_check['legalType']
        except:
            legalType = None
        try:
            shortName = info_check['shortName']
        except:
            shortName = None
        try:
            longName = info_check['longName']
        except:
            longName = None
        try:
            currency = info_check['currency']
        except:
            currency = None
        try:
            financialCurrency = info_check['financialCurrency']
        except:
            financialCurrency = None
        try:
            country = info_check['country']
        except:
            country = None
        try:
            market = info_check['market']
        except:
            market = None
        try:
            exchange = info_check['exchange']
        except:
            exchange = None
        try:
            exchangeTimezoneName = info_check['exchangeTimezoneName']
        except:
            exchangeTimezoneName = None
        try:
            exchangeTimezoneShortName = info_check['exchangeTimezoneShortName']
        except:
            exchangeTimezoneShortName = None
        try:
            currentPrice = info_check['currentPrice']
        except:
            currentPrice = None
        try:
            previousClose = info_check['previousClose']
        except:
            previousClose = None
        try:
            regularMarketPrice = info_check['regularMarketPrice']
        except:
            regularMarketPrice = None
        try:
            regularMarketPreviousClose = info_check['regularMarketPreviousClose']
        except:
            regularMarketPreviousClose = None
        try:
            marketCap = info_check['marketCap']
        except:
            marketCap = None
        try:
            beta = info_check['beta']
        except:
            beta = None
        try:
            beta3Year = info_check['beta3Year']
        except:
            beta3Year = None
        try:
            _yield = info_check['yield']
        except:
            _yield = None
        try:
            dividendYield = info_check['dividendYield']
        except:
            dividendYield = None
        try:
            trailingAnnualDividendYield = info_check['trailingAnnualDividendYield']
        except:
            trailingAnnualDividendYield = None
        try:
            fiveYearAvgDividendYield = info_check['fiveYearAvgDividendYield']
        except:
            fiveYearAvgDividendYield = None
        try:
            dividendRate = info_check['dividendRate']
        except:
            dividendRate = None
        try:
            trailingAnnualDividendRate = info_check['trailingAnnualDividendRate']
        except:
            trailingAnnualDividendRate = None
        try:
            lastDividendValue = info_check['lastDividendValue']
        except:
            lastDividendValue = None
        try:
            bookValue = info_check['bookValue']
        except:
            bookValue = None
        try:
            priceToBook = info_check['priceToBook']
        except:
            priceToBook = None
        try:
            enterpriseValue = info_check['enterpriseValue']
        except:
            enterpriseValue = None
        try:
            trailingPE = info_check['trailingPE']
        except:
            trailingPE = None
        try:
            forwardPE = info_check['forwardPE']
        except:
            forwardPE = None
        try:
            trailingEps = info_check['trailingEps']
        except:
            trailingEps = None
        try:
            forwardEps = info_check['forwardEps']
        except:
            forwardEps = None

        tickersymbol.symbol=symbol
        tickersymbol.quoteType=quoteType
        tickersymbol.legalType=legalType
        tickersymbol.shortName=shortName
        tickersymbol.longName=longName
        tickersymbol.currency=currency
        tickersymbol.financialCurrency=financialCurrency
        tickersymbol.country=country
        tickersymbol.market=market
        tickersymbol.exchange=exchange
        tickersymbol.exchangeTimezoneName=exchangeTimezoneName
        tickersymbol.exchangeTimezoneShortName=exchangeTimezoneShortName
        tickersymbol.currentPrice=currentPrice
        tickersymbol.previousClose=previousClose
        tickersymbol.regularMarketPrice=regularMarketPrice
        tickersymbol.regularMarketPreviousClose=regularMarketPreviousClose
        tickersymbol.marketCap=marketCap
        tickersymbol.beta=beta
        tickersymbol.beta3Year=beta3Year
        tickersymbol._yield=_yield
        tickersymbol.dividendYield=dividendYield
        tickersymbol.trailingAnnualDividendYield=trailingAnnualDividendYield
        tickersymbol.fiveYearAvgDividendYield=fiveYearAvgDividendYield
        tickersymbol.dividendRate=dividendRate
        tickersymbol.trailingAnnualDividendRate=trailingAnnualDividendRate
        tickersymbol.lastDividendValue=lastDividendValue
        tickersymbol.bookValue=bookValue
        tickersymbol.priceToBook=priceToBook
        tickersymbol.enterpriseValue=enterpriseValue
        tickersymbol.trailingPE=trailingPE
        tickersymbol.forwardPE=forwardPE
        tickersymbol.trailingEps=trailingEps
        tickersymbol.forwardEps=forwardEps
        tickersymbol.save()

    # 만약에 오류뜨면
    except:
        return False

    return True

def update_price(ticker):
    try:
        ticker_check = yf.Ticker(ticker)
        history_check = ticker_check.history(period="1d")
        price = history_check['Close'].values[0]

        tickersymbol = TickerSymbol.objects.get(symbol=ticker)
        tickersymbol.regularMarketPrice=price
        tickersymbol.save()
    except:
        return False

    return True


def update(request):
    tickersymbols = TickerSymbol.objects.all()
    cryptousds = CryptoUSD.objects.all()
    exchangerates = ExchangeRate.objects.all()
    if request.method == "POST" and request.POST['option'] == "a":
        ticker = request.POST['ticker']
        ticker = ticker.upper()
        is_update = update_tickersymbol(ticker)
        if is_update == True:
            context = {'result' : '성공'}
        else:
            context = {'result' : '실패'}
        return render(request, 'data_market/update.html', context)
    elif request.method == "POST" and request.POST['option'] == "b":
        ticker = request.POST['ticker']
        ticker = ticker.upper()
        is_update = update_price(ticker)
        if is_update == True:
            context = {'result' : '성공'}
        else:
            context = {'result' : '실패'}
        return render(request, 'data_market/update.html', context)
    elif request.method == "POST" and request.POST['option'] == "c":
        ticker = request.POST['ticker']
        ticker = ticker.upper()
        is_update = data_exchangerate(ticker)
        if is_update == True:
            context = {'result' : '성공'}
        else:
            context = {'result' : '실패'}
        return render(request, 'data_market/update.html', context)
    elif request.method == "POST" and request.POST['option'] == "d":
        for tickersymbol in tickersymbols:
            ticker = tickersymbol.symbol
            is_update = update_tickersymbol(ticker)
            if is_update == False:
                id = tickersymbol.id
                context = {'result' : f'id:{id} 에서 실패'}
                return render(request, 'data_market/update.html', context)
        context = {'result' : '성공'}
        return render(request, 'data_market/update.html', context)
    elif request.method == "POST" and request.POST['option'] == "e":
        for cryptousd in cryptousds:
            ticker = cryptousd.symbol
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
    elif request.method == "POST" and request.POST['option'] == "g":
        for tickersymbol in tickersymbols:
            ticker = tickersymbol.symbol
            is_update = update_price(ticker)
            if is_update == False:
                id = tickersymbol.id
                context = {'result' : f'id:{id} 에서 실패'}
                return render(request, 'data_market/update.html', context)
        context = {'result' : '성공'}
        return render(request, 'data_market/update.html', context)
    else:
        return render(request, 'data_market/update.html')