from django.urls import path

from .views import data_tickersymbol

app_name = 'data_market'

urlpatterns = [

    path('data_tickersymbol/', data_tickersymbol, name='data_tickersymbol'),

]