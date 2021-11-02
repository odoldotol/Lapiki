from django.urls import path

from .views import hall, create, open, delete

app_name = 'portfolios'

urlpatterns = [

    path('', hall, name='hall'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('open/<int:id>/', open, name='open'),

]