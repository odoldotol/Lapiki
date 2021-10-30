from django.shortcuts import get_object_or_404, redirect, render 

from .models import Portfolio

from config.views import certify

import datetime

from django.contrib.auth.decorators import login_required


@login_required
def hall(request):
    # 유저의 포트폴리오들을 가져와서 랜더
    portfolio_user = Portfolio.objects.filter(user=request.user)
    context = {'portfolio_user' : portfolio_user}
    return render(request, 'portfolios/hall.html', context)

@login_required
def create(request):
    # 포트폴리오를 생성
    portfolio = Portfolio.objects.create(
        created_at=datetime.datetime.now(),
        user=request.user
    )
    # 메인포트폴리오가 없으면 생성된 포트폴리오를 메인으로 설정
    main_portfolio = Portfolio.objects.filter(user=request.user, is_main=True)
    if len(main_portfolio) == 0:
        portfolio.is_main = True
        portfolio.save()
    return redirect('data_user:quickcreatemenu', portfolio.id)

@login_required
def open(request, id):
    # 요청한 유저와 접근하려는 포트의 유저id가 같은지 증명
    portfolio = get_object_or_404(Portfolio, id=id)
    certi = certify(request.user, portfolio.user)
    if certi == False:
        return redirect('accounts:logout')
    # 
    return render()
