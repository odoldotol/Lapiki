from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required

from data_market.models import TickerSymbol
from data_user.models import PortfoliosAccount, FinancialAccountsTitle
from portfolios.models import Portfolio

from config.views import certify

import yfinance as yf


@login_required
def quickcreate_menu(request, id):
    # 요청한 유저와 접근하려는 포트의 유저id가 같은지 증명
    portfolio = get_object_or_404(Portfolio, id=id)
    certi = certify(request.user, portfolio.user)
    if certi == False:
        return redirect('accounts:logout')
    # 포트id 가지고 랜더
    context = {
        'id_portfolio' : id,
    }
    return render(request, 'data_user/quickcreate_menu.html', context)

@login_required
def quickcreate1(request, id):
    # 요청한 유저와 접근하려는 포트의 유저id가 같은지 증명
    portfolio = get_object_or_404(Portfolio, id=id)
    certi = certify(request.user, portfolio.user)
    if certi == False:
        return redirect('accounts:logout')
    # 메써드가 포스트면
    if request.method == "POST":
        # code 받아서 symbol모델에서 찾아보기
        ticker = request.POST['code']
        symbol = TickerSymbol.objects.filter(ticker=ticker)
        # 없으면
        if len(symbol) == 0:
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
                # 오류 메세지를 context에 추가하여 템플릿 랜더하기
                # 포트폴리오 종속 어카운트와 포트id를 context에 담기
                accounts = PortfoliosAccount.objects.filter(portfolio=portfolio, a=True)
                tickersymbols = TickerSymbol.objects.all()
                context = {
                    'id_portfolio' : id,
                    'accounts' : accounts,
                    'kind' : 'a',
                    'tickersymbols' : tickersymbols,
                    'error': "symbol을 찾을수 없습니다."
                }
                # 작성 템플릿 랜더
                return render(request, 'data_user/quickcreate1.html', context)
        # 있거나 데이터 만들어왔으면 생성진행
        return redirect('home')
    # 머써드가 포스트가 아니면
    else:
        # 포트폴리오 종속 어카운트와 포트id를 context에 담기
        accounts = PortfoliosAccount.objects.filter(portfolio=portfolio, a=True)
        tickersymbols = TickerSymbol.objects.all()
        context = {
            'id_portfolio' : id,
            'accounts' : accounts,
            'kind' : 'a',
            'tickersymbols' : tickersymbols,
        }
        # 작성 템플릿 랜더
        return render(request, 'data_user/quickcreate1.html', context)


def register_account(request, id, kind):
    # 요청한 유저와 접근하려는 포트의 유저id가 같은지 증명
    portfolio = get_object_or_404(Portfolio, id=id)
    certi = certify(request.user, portfolio.user)
    if certi == False:
        return redirect('accounts:logout')
    # 메써드가 포스트면
    if request.method == "POST":
        # 받은 값 변수 생성
        title = request.POST['title']
        nickname = request.POST['nickname']
        # account 생성
        if kind == "a":
            PortfoliosAccount.objects.create(
                portfolio=portfolio,
                a=True,
                c=True,
                title=title,
                nickname=nickname
            )
        return redirect('data_user:quickcreate1', id)
    # 머써드가 포스트가 아니면
    else:
        # 포트id와 조건에 맞는 계좌타이틀을 context에 담기
        if kind == "a":
            titles = FinancialAccountsTitle.objects.filter(a=True)
        elif kind == 'b':
            titles = FinancialAccountsTitle.objects.filter(b=True)
        elif kind == 'c':
            titles = FinancialAccountsTitle.objects.filter(c=True)
        elif kind == 's':
            titles = FinancialAccountsTitle.objects.filter(s=True)
        elif kind == 'p':
            titles = FinancialAccountsTitle.objects.filter(p=True)
        context = {
            'id_portfolio' : id,
            'kind' : kind,
            'titles' : titles
        }
        return render(request, 'data_user/register_account.html', context)