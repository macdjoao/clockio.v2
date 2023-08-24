from rest_framework.decorators import api_view
from rest_framework.response import Response
from clock.models import Clock
from clock.serializers import ClockSerializer
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK


@api_view()
def clocks(request):
    clocks = Clock.objects.all()
    serializer = ClockSerializer(instance=clocks, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view()
def clock(request, id):
    clock = get_object_or_404(Clock, id=id)
    serializer = ClockSerializer(instance=clock)
    return Response(serializer.data, status=HTTP_200_OK)
