from django.urls import path

from .views import quickcreatemenu, quickcreate1, createaccount

app_name = 'data_user'

urlpatterns = [
    path('quickcreatemenu/<int:id>/', quickcreatemenu, name='quickcreatemenu'),
    path('quickcreate1/<int:id>/', quickcreate1, name='quickcreate1'),
    path('createaccount/<int:id>/', createaccount, name='createaccount'),
]