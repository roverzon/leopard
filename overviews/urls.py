from django.conf.urls import url
from overviews import views


urlpatterns = [
    url(r'^api/overviews$', views.overview_list),
    url(r'^api/overviews/(?P<symbol>[\w\-]+)$', views.overview_detail),
    url(r'^api/overview_init$', views.overview_init),
    url(r'^api/overview_all_init/(?P<symbol>[\w\-]+)$', views.overview_all),
    url(r'^api/pg/vX/overview_all_init$', views.overview_init_from_polygon),
]
