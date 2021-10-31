from django.urls import path

from .views import quickcreate_menu, quickcreate1, register_account

app_name = 'data_user'

urlpatterns = [
    path('quickcreate_menu/<int:id>/', quickcreate_menu, name='quickcreate_menu'),
    path('quickcreate1/<int:id>/', quickcreate1, name='quickcreate1'),
    path('register_account/<int:id>/<str:kind>/', register_account, name='register_account'),
]