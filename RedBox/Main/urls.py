from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie/(?P<id>\d+)/$', views.movie_detail, name='movie_detail'),
    url(r'^game/(?P<id>\d+)/$', views.game_detail, name='game_detail'),
]

#index = product_list