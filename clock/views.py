from rest_framework.decorators import api_view
from clock.services import ClockService
from rest_framework.parsers import JSONParser

service = ClockService()


@api_view()
def clocks(request):
    return service.read_list()


# TODO: Method POST Not Allowed
@api_view(http_method_names=['GET', 'POST', 'PATCH', 'DELETE'])
def clock(request, id: int = None):
    if request.method == 'GET':
        return service.read_one(id=id)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        return service.create(data=data)
