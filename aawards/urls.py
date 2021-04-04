from django.urls import path
from . import views
from . views import index 

urlpatterns = [
    path('',index, name='home'),
    path('register/',views.register, name='registration'),
    path('search/', views.searchprofile, name='search'),
]