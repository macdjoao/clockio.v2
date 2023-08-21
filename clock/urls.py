from clock import views
from django.urls import path

urlpatterns = [
    path('api/home', views.hello_world)
]
