from django.conf.urls import url
from cash_flows import views

urlpatterns = [
    url(r'^api/cashflows$', views.cashflow_list),
    url(r'^api/cashflows/(?P<symbol>[\w\-]+)$', views.symbol_cashflow_list),
    url(r'^api/cashflow_init/annualReport$', views.cashflow_init_annual),
    url(r'^api/cashflow_init/quarterlyReport$', views.cashflow_init_quarterly),
]
