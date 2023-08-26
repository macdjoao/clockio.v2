from rest_framework.decorators import api_view
from rest_framework.response import Response
from clock.models import Clock
from clock.serializers import ClockOutSerializer
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK
from clock.services import ClockService


service = ClockService()


@api_view()
def clocks(request):
    return service.read_list()


@api_view()
def clock(request, id: int):
    clock = get_object_or_404(Clock, id=id)
    serializer = ClockOutSerializer(instance=clock)
    return Response(serializer.data, status=HTTP_200_OK)
