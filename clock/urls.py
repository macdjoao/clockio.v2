from django.urls import path

from clock import views


urlpatterns = [
    path('api/clocks', views.clock_without_id, name='clocks-without-id'),
    path('api/clocks/<int:id>', views.clock_with_id, name='clocks-without-id'),
]
