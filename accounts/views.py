from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout




def logout(request):
    auth_logout(request)
    return redirect('home')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect('entry')

        else:
            context = {'error': "아이디 또는 비밀번호가 일치하지 않습니다."}
            return render(request, 'accounts/login.html', context)

    else:
        return render(request, 'accounts/login.html')

def login_next(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        url = request.POST.get('next')
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect(url)

        else:
            context = {'error': "아이디 또는 비밀번호가 일치하지 않습니다."}
            return render(request, 'accounts/login.html', context)

    else:
        next = request.GET.get('next')
        context = {'next': next}
        return render(request, 'accounts/login.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            user = authenticate(request, username=username, password=password)
            auth_login(request, user)

            return redirect('portfolios:hall')

        else:
            context = {'error': "비밀번호가 일치하지 않습니다."}
            return render(request, "accounts/signup.html", context)
    else:
        return render(request, 'accounts/signup.html')