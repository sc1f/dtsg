from django.conf.urls import url

from . import views

urlpatterns = [
    # index page for elections
    url(r'^$', views.index, name='index'),
    # get election by year
    url(r'^(?P<year>[0-9]{4})/$', views.election, name='election'),
    # get race by election year
    url(r'^(?P<year>[0-9]{4})/race/(?P<race_id>[0-9])/$', views.race, name='race'),
    # get candidate by year and id
    url(r'^(?P<year>[0-9]{4})/(?P<race_id>[0-9])/candidate/(?P<candidate_id>[0-9])/$', views.candidate, name='candidate')
]