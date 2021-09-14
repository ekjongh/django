from django.urls import path
from article import views

urlpatterns = [
    path('main/', views.main), 
    path('predict/', views.predict), 

]
