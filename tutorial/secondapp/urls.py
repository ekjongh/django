from django.contrib import admin
from django.urls import path
from secondapp import views

app_name = 'secondapp'
urlpatterns = [

    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show, name='show'),
    path('showArmyShop/', views.showArmyShop, name='showArmyShop'),
    path('showArmyShop/<int:year>/<int:month>/', views.showArmyShop2, name='showArmyShop2'),

    path('req/ajax/exam/', views.req_ajax_exam),
    path('req/ajax/get/', views.req_ajax_get, name='ajax_get'),
    path('req/ajax/post/', views.req_ajax_post, name='ajax_post'),
    path('req/ajax/json/', views.req_ajax_json, name='ajax_json'),

    path('course/create/', views.course_create),

]

