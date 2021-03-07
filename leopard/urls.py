from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin', admin.site.urls),
    url(r'^', include('overviews.urls')),
    url(r'^', include('income_statements.urls')),
    url(r'^', include('cash_flows.urls')),
    url(r'^', include('balance_statements.urls')),
    url(r'^', include('open_and_close.urls')),
    url(r'^', include('portfolios.urls')),
    url(r'^', include('positions.urls')),
    url(r'^', include('watchlists.urls')),
    url(r'^', include('tickers.urls')),
    url(r'^api-token-auth$', obtain_jwt_token),
    url(r'^api-token-refresh$', refresh_jwt_token),
]
