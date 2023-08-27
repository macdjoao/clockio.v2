from rest_framework.decorators import api_view
from clock.services import ClockService
from rest_framework.response import Response

service = ClockService()


@api_view(['GET'])
def clocks(request):
    if request.method == 'GET':
        return service.read_list()


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def clock(request, id: int):
    if request.method == 'GET':
        return service.read_one(id=id)
    if request.method == 'POST':
        return Response({'method': 'post'})
    if request.method == 'PATCH':
        return Response({'method': 'patch'})
    if request.method == 'DELETE':
        return Response({'method': 'delete'})
