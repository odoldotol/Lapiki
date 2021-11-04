from django.urls import path

from .views import hall, create, open, delete, main

app_name = 'portfolios'

urlpatterns = [

    path('', hall, name='hall'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('main/<int:id>/', main, name='main'),
    path('open/<int:id>/', open, name='open'),
]