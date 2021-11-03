from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required

from data_market.models import TickerSymbol
from .models import AccountsAsset, AssetsAction, PortfoliosAccount
from portfolios.models import Portfolio
from data_support.models import AssetFormat, FinancialAccountsTitle

from config.views import certification
from data_market.views import data_tickersymbol


@login_required
def quickcreate_menu(request, id):
    # 증명
    portfolio = get_object_or_404(Portfolio, id=id, is_deleted=False)
    certi = certification(request, portfolio)
    if certi == False:
        return redirect('accounts:logout')
    # 포트id 가지고 랜더
    context = {
        'id_portfolio' : id,
    }
    return render(request, 'data_user/quickcreate_menu.html', context)

@login_required
def quickcreate1(request, id):
    # 증명
    portfolio = get_object_or_404(Portfolio, id=id, is_deleted=False)
    certi = certification(request, portfolio)
    if certi == False:
        return redirect('accounts:logout')
    # 메써드가 포스트이고 작성이 완료가 안됬으면
    if request.method == "POST" and request.POST['complete'] == "n":
        # code 받아서 symbol모델에서 찾아보기
        code = request.POST['code']
        code = code.lower()
        symbol = TickerSymbol.objects.filter(ticker=code)
        # 없으면
        if len(symbol) == 0:
            # 새로 만들어봐!
            data_symbol = data_tickersymbol(code)
            # 못만들어왔으면
            if data_symbol == False:
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
        ##### 있거나 만들어왔으면 생성할 모델들의 재료들을 기록해두고 다시 랜더하기
        list_for_create = []
        try:
            len_list = int(request.POST['len_list'])
            for i in range(len_list):
                account_id = request.POST[f'account_id{i}']
                ticker = request.POST[f'ticker{i}']
                shortName = request.POST[f'shortName{i}']
                amount = request.POST[f'amount{i}']
                dic = {}
                dic['account_id'] = account_id
                dic['ticker'] = ticker
                dic['shortName'] = shortName
                dic['amount'] = amount
                list_for_create = list_for_create + [dic]
        except:
            pass
        account_id = request.POST['account']
        selected_maker = request.POST['account']
        tickersymbol = get_object_or_404(TickerSymbol, ticker=code)
        shortName = tickersymbol.shortName
        amount = request.POST['amount']
        dic = {}
        dic['account_id'] = account_id
        dic['ticker'] = code
        dic['shortName'] = shortName
        dic['amount'] = amount
        list_for_create = list_for_create + [dic]
        len_list = len(list_for_create)
        ##### context 만들고 랜더
        ### context 만들기
        # 포트폴리오 종속 어카운트와 포트id를 context에 담기
        accounts = PortfoliosAccount.objects.filter(portfolio=portfolio, a=True)
        tickersymbols = TickerSymbol.objects.all()
        context = {
            'id_portfolio' : id,
            'accounts' : accounts,
            'kind' : 'a',
            'tickersymbols' : tickersymbols,
            'len_list' : len_list,
            'list_for_create' : list_for_create,
            'selected_maker' : selected_maker,
        }
        ### 랜더
        return render(request, 'data_user/quickcreate1.html', context)
    # 메써드가 포스트 이고 작성이 완료됬으면 asset 과 action 만들기
    elif request.method == "POST" and request.POST['complete'] == "y":
        len_list = int(request.POST['len_list'])
        for i in range(len_list):
            account_id = request.POST[f'account_id{i}']
            ticker = request.POST[f'ticker{i}']
            amount = request.POST[f'amount{i}']
            # symbol모델에서 찾아오기
            tickersymbol = get_object_or_404(TickerSymbol, ticker=ticker)
            ##### asset 만들기
            account = get_object_or_404(PortfoliosAccount, id=account_id)
            code = tickersymbol.symbol
            name = tickersymbol.longName
            format = get_object_or_404(AssetFormat, title='주식')
            # 계좌에 동일역할 asset이 이미 있는지 확인
            check = AccountsAsset.objects.filter(account=account, format=format, code=code)
            # 없을떄만 생성
            if len(check) == 0:
                AccountsAsset.objects.create(
                    account=account,
                    format=format,
                    code=code,
                    name=name,
                    portfolio=portfolio
                )
            # action 만들기
            asset = get_object_or_404(AccountsAsset, account=account, format=format, code=code)
            amount_buy = amount
            AssetsAction.objects.create(
                asset_buy=asset,
                amount_buy=amount_buy,
                rabel='IO',
                account_buy=account,
                portfolio=portfolio
            )
        # 
        return redirect('data_user:quickcreate_menu', id)
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
    # 증명
    portfolio = get_object_or_404(Portfolio, id=id, is_deleted=False)
    certi = certification(request, portfolio)
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