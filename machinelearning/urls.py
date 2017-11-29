from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^(?P<algorithm_code>[a-zA-Z]+)/(?P<dataset>[a-zA-Z]+)/$', views.algorithm, name='algorithm'),
 url(r'^algorithms/', views.AlgorithmList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)