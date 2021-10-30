from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from data_user.models import PortfoliosAccount
from portfolios.models import Portfolio, AccountFormat

from config.views import certify


@login_required
def quickcreatemenu(request, id):
    # 요청한 유저와 접근하려는 포트의 유저id가 같은지 증명
    portfolio = get_object_or_404(Portfolio, id=id)
    certi = certify(request.user, portfolio.user)
    if certi == False:
        return redirect('accounts:logout')
    # 포트id 가지고 랜더
    context = {
        'id_portfolio' : id,
    }
    return render(request, 'data_user/quickcreatemenu.html', context)

@login_required
def quickcreate1(request, id):
    # 요청한 유저와 접근하려는 포트의 유저id가 같은지 증명
    portfolio = get_object_or_404(Portfolio, id=id)
    certi = certify(request.user, portfolio.user)
    if certi == False:
        return redirect('accounts:logout')
    # 포트폴리오 종속 어카운트와 포트id를 context에 담기
    portfoliosaccounts = PortfoliosAccount.objects.filter(portfolio=portfolio)
    context = {
        'id_portfolio' : id,
        'portfoliosaccounts' : portfoliosaccounts
    }
    # 메써드가 포스트면
    if request.method == "POST":
        pass
    # 머써드가 포스트가 아니면 작성 템플릿 랜더
    else:
        return render(request, 'data_user/quickcreate1.html', context)

def createaccount(request, id):
    # 요청한 유저와 접근하려는 포트의 유저id가 같은지 증명
    portfolio = get_object_or_404(Portfolio, id=id)
    certi = certify(request.user, portfolio.user)
    if certi == False:
        return redirect('accounts:logout')
    # 어카운트포멧과 포트id를 context에 담기
    accountsformats = AccountFormat.objects.all()
    context = {
        'id_portfolio' : id,
        'accountsformats' : accountsformats
    }
    # 메써드가 포스트면
    if request.method == "POST":
        pass
    # 머써드가 포스트가 아니면 작성 템플릿 랜더
    else:
        return render(request, 'data_user/createaccount.html', context)