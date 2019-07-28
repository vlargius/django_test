from django.urls import path

from . import views

app_name = 'marks'
urlpatterns = [
    path('test', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
]
