from django.conf.urls import url
from . import views

urlpatterns = [
    url('test/$', views.TestAPIView.as_view()),
    url('test/?P<pk>.*/$', views.TestAPIView.as_view())
]