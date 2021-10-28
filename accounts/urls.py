from django.urls import path

from .views import signup, login, logout, login_next

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('login_next/', login_next, name="login_next"),
    path('logout/', logout, name="logout"),
]
