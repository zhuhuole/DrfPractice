from django.conf.urls import url
from . import views

urlpatterns = [
    url('test/$', views.TestView.as_view()),
    url('test/?P<pk>.*/$', views.TestView.as_view())
]