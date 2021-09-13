from django.contrib import admin
from django.urls import path
from secondapp import views

urlpatterns = [

    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('showArmyShop/', views.showArmyShop),
    
]
