from django.contrib import admin
from django.urls import path

from django.urls.conf import include

from .views import entry, home

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', home, name="home"),
    path('', entry, name="entry"),


    path('portfolios/', include("portfolios.urls")),
    path('accounts/', include("accounts.urls")),
    path('data_user/', include("data_user.urls")),
    path('data_market/', include("data_market.urls")),
    path('data_portfolio/', include("data_portfolio.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)