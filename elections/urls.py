from django.conf.urls import url

from . import views

urlpatterns = [
    # index page for elections
    url(r'^$', views.races, name='races'),
    # get election by year
    #url(r'^(?P<year>[0-9]{4})/$', views.races, name='races'), # 4/23/2018: fixed the url, removed the year view
    # get race by election year
    url(r'^(?P<year>[0-9]{4})/race/(?P<race_id>[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/$', views.positions, name='positions'),
    # get position and related candidates by year and id
    url(r'^(?P<year>[0-9]{4})/(?P<race_id>[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(?P<position_id>[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/$', views.candidates, name='candidates'),
    # candidate surveys
    url(r'^(?P<year>[0-9]{4})/add_candidate/$', views.add_candidate, name='add_candidate'),
]