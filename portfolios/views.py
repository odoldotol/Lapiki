from django.shortcuts import get_object_or_404, redirect, render

from data_portfolio.models import DataPortfolio 
from .models import Portfolio

from config.views import certification

import datetime

from django.contrib.auth.decorators import login_required


@login_required
def hall(request):
    # 유저의 포트폴리오들을 가져와서 랜더
    portfolios = Portfolio.objects.filter(user=request.user, is_deleted=False)
    len_portfolios = len(portfolios)
    context = {
        'portfolios' : portfolios,
        'len_portfolios' : len_portfolios,
    }
    return render(request, 'portfolios/hall.html', context)

@login_required
def create(request):
    # 포트폴리오를 생성
    portfolios = Portfolio.objects.filter(user=request.user, is_deleted=False)
    if len(portfolios) < 2:
        portfolio = Portfolio.objects.create(
            created_at=datetime.datetime.now(),
            user=request.user
        )
        DataPortfolio.objects.create(
            portfolio=portfolio,
            is_main=True
        )
    else:
        return redirect('accounts:logout')
    # 메인포트폴리오가 없으면 생성된 포트폴리오를 메인으로 설정
    main_portfolio = Portfolio.objects.filter(user=request.user, is_main=True, is_deleted=False)
    if len(main_portfolio) == 0:
        portfolio.is_main = True
        portfolio.save()
    return redirect('portfolios:hall')

def delete(request, id):
    # 증명
    portfolio = get_object_or_404(Portfolio, id=id, is_deleted=False)
    certi = certification(request, portfolio)
    if certi == False:
        return redirect('accounts:logout')
    # 삭제
    portfolio.is_deleted=True
    portfolio.save()
    # 
    return redirect('portfolios:hall')

def main(request, id):
    # 증명
    portfolio = get_object_or_404(Portfolio, id=id, is_deleted=False)
    certi = certification(request, portfolio)
    if certi == False:
        return redirect('accounts:logout')
    # 메인이면 메인해제 메인아니면 메인설정하고 다른 메인인 포트 메인해제
    portfolio_is_main = portfolio.is_main
    if portfolio_is_main == True:
        portfolio.is_main=False
        portfolio.save()
    elif portfolio_is_main == False:
        main_portfolios = Portfolio.objects.filter(user=request.user, is_main=True, is_deleted=False)
        if len(main_portfolios) == 1:
            main_portfolio = get_object_or_404(Portfolio, user=request.user, is_main=True, is_deleted=False)
            main_portfolio.is_main=False
            main_portfolio.save()
        portfolio.is_main=True
        portfolio.save()
    return redirect('portfolios:hall')

@login_required
def open(request, id):
    # 증명
    portfolio = get_object_or_404(Portfolio, id=id, is_deleted=False)
    certi = certification(request, portfolio)
    if certi == False:
        return redirect('accounts:logout')
    # 
    return render()
