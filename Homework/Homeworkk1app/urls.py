from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),\
    #
    path('', views.index, name='home'),
    path('home', views.home, name='home'),
    path('about_me', views.about_me, name='about_me')

]