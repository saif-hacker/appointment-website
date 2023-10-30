from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('service/',views.service),
    path('about/',views.about),
    path('contact/',views.contact),
    path('sign_up/',views.Sign_up)
    
]
