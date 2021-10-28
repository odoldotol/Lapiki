from django.shortcuts import redirect, render 

from portfolios.models import Portfolio


def entry(request):
    # 로그인 되어있으면 메인포트가 있는지보고 메인포트로 보내
    if request.user.is_authenticated:
        mainportfolio = Portfolio.objects.filter(user=request.user, is_main=True)
        if len(mainportfolio) == 1:
            id = mainportfolio[0].id
            return redirect('portfolios:open', id)
        # 메인포트도 설정 안되있으면 hall로 리다이렉트
        else:
            return redirect('portfolios:hall')
    # 로그인 안되어있으면 홈으로
    else:
        return redirect('home')

def home(request):
    return render(request, 'home.html')







def certify(request_user, portfolio_user):
    if request_user == portfolio_user:
        return True
    else:
        return False