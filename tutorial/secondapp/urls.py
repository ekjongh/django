from django.contrib import admin
from django.urls import path
from secondapp import views

urlpatterns = [

    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('showArmyShop/', views.showArmyShop),
    path('showArmyShop/<int:year>/<int:month>/', views.showArmyShop2),

    path('req/ajax/', views.req_ajax),
    path('req/ajax/get1', views.req_ajax_get),
    path('req/ajaxp/post1', views.req_ajax_post),
    path('req/ajaxj/json', views.req_ajax_json),


]

