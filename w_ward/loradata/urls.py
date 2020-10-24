from django.urls import path
from . import views

app_name = 'loradata'
urlpatterns = [
    path('',views.index,name="index"),
    path('loradata', views.IndexView.as_view(),name='index'),
]