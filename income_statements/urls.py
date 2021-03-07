from django.conf.urls import url
from income_statements import views


urlpatterns = [
    url(r'^api/incomes$', views.income_list),
    url(r'^api/incomes/(?P<symbol>[\w\-]+)$', views.symbol_income_list),
    url(r'^api/incomes/(?P<symbol>[\w\-]+)/(?P<fyear>[0-9]+)$', views.symbol_income_detail),
    url(r'^api/income_init/annualReport$', views.income_init_annual),
    url(r'^api/income_init/quarterlyReport$', views.income_init_quarterly),
]
