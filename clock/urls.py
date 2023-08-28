from clock import views
from django.urls import path

urlpatterns = [
    path('api/get_clocks', views.get_clocks, name='get-clocks'),
    path('api/get_clock/<int:id>', views.get_clock, name='get-clock'),
    path('api/post_clock', views.post_clock, name='post-clock'),
    path('api/patch_clock/<int:id>', views.update_clock, name='patch-clock'),
    path('api/delete_clock/<int:id>', views.delete_clock, name='delete-clock'),
]
