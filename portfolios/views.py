from django.shortcuts import get_object_or_404, redirect, render

from data_portfolio.views import com_dataportfolio_market_preclose, complete_assets, data_portfolio_main, order_chartdata_by_value
from config.views import certification
from visualizing.views import save_main_piechart

from data_portfolio.models import DataPortfolio
from .models import Portfolio

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
    # com asset
    now = datetime.datetime.now()
    is_com = complete_assets(id, now)
    if is_com == False:
        return redirect('fail')
    # data 포트폴리오 수정하기
    dataportfolio = data_portfolio_main(portfolio)
    if dataportfolio == False:
        return redirect('fail')
    # 마켓 테이터 이용하여 차트 데이터 만들기
    list_list_chartdata = com_dataportfolio_market_preclose(dataportfolio)
    if list_list_chartdata == False:
        return redirect('fail')
    # 차트 데이터 정렬하기
    list_chartdata_stockthing = list_list_chartdata[0]
    list_chartdata_crypto = list_list_chartdata[1]
    list_chartdata_cash = list_list_chartdata[2]
    list_chartdata_saving = list_list_chartdata[3]
    ordered_chartdata_stockthing = order_chartdata_by_value(list_chartdata_stockthing)
    if ordered_chartdata_stockthing == False:
        return redirect('fail')
    ordered_chartdata_crypto = order_chartdata_by_value(list_chartdata_crypto)
    if ordered_chartdata_crypto == False:
        return redirect('fail')
    ordered_chartdata_cash = order_chartdata_by_value(list_chartdata_cash)
    if ordered_chartdata_cash == False:
        return redirect('fail')
    ordered_chartdata_saving = order_chartdata_by_value(list_chartdata_saving)
    if ordered_chartdata_saving == False:
        return redirect('fail')
    # 메인 파이차트 저장하기
    value_list = ordered_chartdata_stockthing[0]
    label_list = ordered_chartdata_stockthing[1]
    naming = 'stockthing'
    chartmaker = save_main_piechart(value_list, label_list, id, naming)
    if chartmaker == False:
        return redirect('fail')
    value_list = ordered_chartdata_crypto[0]
    label_list = ordered_chartdata_crypto[1]
    naming = 'crypto'
    chartmaker = save_main_piechart(value_list, label_list, id, naming)
    if chartmaker == False:
        return redirect('fail')
    value_list = ordered_chartdata_cash[0]
    label_list = ordered_chartdata_cash[1]
    naming = 'cash'
    chartmaker = save_main_piechart(value_list, label_list, id, naming)
    if chartmaker == False:
        return redirect('fail')
    value_list = ordered_chartdata_saving[0]
    label_list = ordered_chartdata_saving[1]
    naming = 'saving'
    chartmaker = save_main_piechart(value_list, label_list, id, naming)
    if chartmaker == False:
        return redirect('fail')
    value_list = [dataportfolio.stockthing] + [dataportfolio.crypto] + ordered_chartdata_cash[0]
    label_list = ['stock'] + ['crypto'] + ordered_chartdata_cash[1]
    naming = 'stock_crypto_cash'
    chartmaker = save_main_piechart(value_list, label_list, id, naming)
    if chartmaker == False:
        return redirect('fail')
    value_list = [dataportfolio.stockthing] + [dataportfolio.crypto] + [dataportfolio.saving] + [dataportfolio.cash]
    label_list = ['stock'] + ['crypto'] + ['saving'] + ['cash']
    naming = 'stock_crypto_saving_cash'
    chartmaker = save_main_piechart(value_list, label_list, id, naming)
    if chartmaker == False:
        return redirect('fail')

    context = {
        'portfolio_id' : id,
    }
    return render(request, 'portfolios/main.html', context)

    