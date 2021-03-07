from django.conf.urls import url
from open_and_close import views


urlpatterns = [
    url(r'^api/trading/(?P<symbol>[\w\-]+)$', views.open_and_close_detail),
    url(r'^api/trading_init/(?P<symbol>[\w\-]+)$', views.open_and_close_detail_init),
]