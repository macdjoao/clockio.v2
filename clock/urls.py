from django.urls import path

from clock import views


urlpatterns = [
    # CBV URLs (APIView)
    path('api/clocks', views.ClockWithoutIdAPIView.as_view(),
         name='clocks-without-id'),
    path('api/clocks/<int:id>', views.ClockWithIdAPIView.as_view(),
         name='clocks-without-id')

    # FBV URLs
    # path('api/clocks', views.clock_without_id, name='clocks-without-id'),
    # path('api/clocks/<int:id>', views.clock_with_id, name='clocks-without-id')
]
