from clock import views
from django.urls import path

urlpatterns = [
    path('api/clock', views.clocks, name='api-clocks'),
    path('api/clock/<int:id>', views.clock, name='api-clock-id')
]
