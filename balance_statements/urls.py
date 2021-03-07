from django.conf.urls import url
from balance_statements import views


urlpatterns = [
    url(r'^api/balancesheets$', views.balancesheet_list),
    url(r'^api/balancesheets/(?P<symbol>[\w\-]+)$', views.symbol_balancesheet_list),
    url(r'^api/balancesheet_init/annualReport$', views.balancesheet_init_annual),
    url(r'^api/balancesheet_init/quarterlyReport$', views.balancesheet_init_quarterly),
]
