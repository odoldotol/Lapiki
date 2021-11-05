from django.urls import path

from .views import quickcreate0, quickcreate1, quickcreate2, quickcreate3, quickcreate_menu, register_account

app_name = 'data_user'

urlpatterns = [
    path('quickcreate_menu/<int:id>/', quickcreate_menu, name='quickcreate_menu'),
    path('quickcreate0/<int:id>/', quickcreate0, name='quickcreate0'),
    path('quickcreate1/<int:id>/', quickcreate1, name='quickcreate1'),
    path('quickcreate2/<int:id>/', quickcreate2, name='quickcreate2'),
    path('quickcreate3/<int:id>/', quickcreate3, name='quickcreate3'),
    path('register_account/<int:id>/<str:kind>/', register_account, name='register_account'),
]