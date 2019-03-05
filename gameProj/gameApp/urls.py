from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/delete/<int:id>/', views.deleteaccount, name='delete'),
    path('/editgame/<int:id>/', views.editgame, name='editgame'),
    path('/creategame', views.creategame, name='creategame'),
    path('/createuser', views.createuser, name='createuser'),
    path('accounts/', include('django.contrib.auth.urls')),
]