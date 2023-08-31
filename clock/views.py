from django.shortcuts import get_list_or_404, get_object_or_404
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from clock.models import Clock
from clock.serializers import ClockOutSerializer, ClockInSerializer


# CBV - Class Based Views (APIView)

class ClockWithIdAPIView(APIView):

    def get_clock(self, id: int):
        clock = get_object_or_404(Clock, id=id)
        return clock

    def get(self, request, id: int):
        clock = self.get_clock(id)
        serializer = ClockOutSerializer(instance=clock)
        return Response(serializer.data, status=HTTP_200_OK)

    # TODO
    def patch(self, request, id: int):
        pass

    def delete(self, request, id: int):
        clock = self.get_clock(id)
        clock.delete()
        return Response({'detail': 'Clock successfully deleted'}, status=HTTP_204_NO_CONTENT)


class ClockWithoutIdAPIView(APIView):

    def get(self, request):
        clocks = get_list_or_404(Clock)
        serializer = ClockOutSerializer(instance=clocks, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = ClockInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Clock successfully created'}, status=HTTP_201_CREATED)


# FBV - Function Based Views

# @api_view(['GET', 'PATCH', 'DELETE'])
# def clock_with_id(request, id: int):

#     clock = get_object_or_404(Clock, id=id)

#     if request.method == 'GET':
#         serializer = ClockOutSerializer(instance=clock)
#         return Response(serializer.data, status=HTTP_200_OK)

#     # TODO
#     if request.method == 'PATCH':
#         pass

#     if request.method == 'DELETE':
#         clock.delete()
#         return Response({'detail': 'Clock successfully deleted'}, status=HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def clock_without_id(request):

#     if request.method == 'GET':
#         clocks = get_list_or_404(Clock)
#         serializer = ClockOutSerializer(instance=clocks, many=True)
#         return Response(serializer.data, status=HTTP_200_OK)

#     if request.method == 'POST':
#         serializer = ClockInSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'detail': 'Clock successfully created'}, status=HTTP_201_CREATED)
