from django.conf.urls import url
from watchlists import views

urlpatterns = [
    url(r'^api/watchlists$', views.watchlist_list),
    url(r'^api/watchlists/create$', views.watchlist_create),
]
