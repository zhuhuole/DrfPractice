from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.BookAPIView.as_view()),
    url(r'^books/(?P<pk>.*)/$', views.BookAPIView.as_view())
]