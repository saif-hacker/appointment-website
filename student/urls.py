from django.urls import path
from student import views
from django.contrib import admin

urlpatterns = [
    path('',views.home),
    path('service/',views.service),
    path('about/',views.about),
    path('contact/',views.contact),
    path('sign_up/',views.sign_up),
    # path('login/',views.Login),
    
]
