from django.contrib import admin
from django.urls import path
from secondapp import views

urlpatterns = [

    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('showArmyShop/', views.showArmyShop),
    path('showArmyShop/<int:year>/<int:month>/', views.showArmyShop2),

    path('req/ajax/exam', views.req_ajax_exam),
    path('req/ajax/get/', views.req_ajax_get),
    path('req/ajax/post/', views.req_ajax_post),
    path('req/ajax/json/', views.req_ajax_json),

]

