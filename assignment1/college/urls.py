from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('cse', views.cse,name="cse" ),
    path('mech', views.mech,name="mech" ),
    path('entc', views.entc,name="entc" ),
    path('civil', views.civil,name="civil" )
]
