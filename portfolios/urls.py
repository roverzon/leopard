from django.conf.urls import url
from portfolios import views

urlpatterns = [
    url(r'^api/portfolios$', views.portfolio_list),
    url(r'^api/portfolios/create$', views.portfolio_create),
]
