# stocks/urls.py
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^intraday/(?P<symbol>\w+)/?$', IntradayStock.as_view()),
    re_path(r'^daily/(?P<symbol>\w+)/?$', DailyStock.as_view()),
    re_path(r'^search/(?P<symbol>\w+)/?$', SearchStock.as_view()),
]
