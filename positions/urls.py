from django.conf.urls import url
from positions import views

urlpatterns = [
    url(r'^api/positions$', views.positions_list),
    url(r'^api/positions/create$', views.position_create),
]
