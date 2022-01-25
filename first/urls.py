from django.urls import path
#from .wonder import views
from . import views
from .views import index
from .views import abc

urlpatterns = [
    path('', index, name='index'),
    path('index2/', abc, name='abc'),
    #path('',, name='indexx'),
    #path()
    path('wtf/', views.functionh, name='functionh'),
    path('home/', views.homerender, name='homerender'),
    path('logout/', views.loggedout, name='loggedout')
]
