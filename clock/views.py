from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK

from clock.models import Clock
from clock.serializers import ClockOutSerializer, ClockInSerializer


@api_view(['GET'])
def get_clocks(request):
    clocks = get_list_or_404(Clock)
    serializer = ClockOutSerializer(instance=clocks, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_clock(request, id: int):
    clock = get_object_or_404(Clock, id=id)
    serializer = ClockOutSerializer(instance=clock)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def post_clock(request):
    serializer = ClockInSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'detail': 'Clock successfully created'}, status=HTTP_201_CREATED)


@api_view(['PATCH'])
def update_clock(request, id: int):
    return Response({'method': 'patch'})


@api_view(['DELETE'])
def delete_clock(request, id: int):
    return Response({'method': 'delete'})
