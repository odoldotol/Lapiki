from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required

from data_user.models import PortfoliosAccount, FinancialAccountsTitle
from portfolios.models import Portfolio

from config.views import certify


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
        pass
    else:
        # 포트폴리오 종속 어카운트와 포트id를 context에 담기
        accounts = PortfoliosAccount.objects.filter(portfolio=portfolio, a=True)
        context = {
            'id_portfolio' : id,
            'accounts' : accounts,
            'kind' : 'a'
        }
        # 머써드가 포스트가 아니면 작성 템플릿 랜더
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