from django.urls import path

from .views import hall, create, open

app_name = 'portfolios'

urlpatterns = [

    path('', hall, name='hall'),
    path('create/', create, name='create'),
    path('open/<int:id>/', open, name='open'),

]