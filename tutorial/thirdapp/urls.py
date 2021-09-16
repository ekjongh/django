from django.urls import path
from . import views

app_name= 'thirdapp'
urlpatterns = [
    path('shop/', views.shop),
    path('jeju_olle/', views.jeju_olle, name='jeju_olle'),
]