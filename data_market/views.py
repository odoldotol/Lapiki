from django.shortcuts import render

from .models import TickerSymbol

import yfinance as yf



def data_tickersymbol(ticker):
    # 존재하는 symbol이라 가정하고 진행
    try:
        # symbol모델로 데이터만들기
        ticker_check = yf.Ticker(ticker)
        info_check = ticker_check.info
        TickerSymbol.objects.create(
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
            trailingPE=info_check['trailingPE'],
            dividendYield=info_check['dividendYield'],
            trailingEps=info_check['trailingEps'],
            beta=info_check['beta'],
            currentPrice=info_check['currentPrice']
        )
    # 만약에 오류뜨면
    except:
        return False
    return True
