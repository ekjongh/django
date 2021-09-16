from django.contrib import admin
from django.urls import path
from firstapp import views

app_name = 'firstapp' # namespace
urlpatterns = [

    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show, name='show'),

    path('req/get/', views.req_get),
    path('req/post/', views.req_post),

    path('req/ajax1/', views.req_ajax1),
    path('req/ajax2/', views.req_ajax2),

    path('req/json/', views.req_json),

    path('req/ajax4/', views.req_ajax4),

    path('static/', views.static),
    path('var/', views.var),
    path('tag/', views.tag),
    path('custom_filter/', views.custom_filter),

    path('template/', views.template),

    path('form/basic/', views.form_basic),
    path('form/model/', views.form_model),

]
