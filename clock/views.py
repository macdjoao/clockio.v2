from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT

from clock.models import Clock
from clock.serializers import ClockOutSerializer, ClockInSerializer


@api_view(['GET', 'PATCH', 'DELETE'])
def clock_with_id(request, id: int):
    clock = get_object_or_404(Clock, id=id)
    if request.method == 'GET':
        serializer = ClockOutSerializer(instance=clock)
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method == 'PATCH':
        # TODO
        # serializer = ClockInSerializer(
        #     instance=clock, data=request.data, partial=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response({'method': 'patch'})
    if request.method == 'DELETE':
        clock.delete()
        return Response({'detail': 'Clock successfully deleted'}, status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def clock_without_id(request):
    if request.method == 'GET':
        clocks = get_list_or_404(Clock)
        serializer = ClockOutSerializer(instance=clocks, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    if request.method == 'POST':
        serializer = ClockInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Clock successfully created'}, status=HTTP_201_CREATED)
