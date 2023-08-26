from rest_framework.decorators import api_view
from clock.services import ClockService

service = ClockService()


@api_view()
def clocks(request):
    return service.read_list()


@api_view(http_method_names=['GET', 'POST', 'PATCH', 'DELETE'])
def clock(request, id: int):
    if request.method == 'GET':
        return service.read_one(id=id)
