from django.shortcuts import get_object_or_404
from clock.models import Clock
from clock.serializers import ClockInSerializer, ClockOutSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.response import Response


class ClockService:
    def __init__(self) -> None:
        self.queryset = Clock.objects.all()

    # TODO
    def create(self, data: dict):
        serializer = ClockInSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Clock successfully created'}, status=HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'detail': 'Invalid payload'}, status=HTTP_400_BAD_REQUEST)

    def read_list(self):
        if self.queryset:
            serializer = ClockOutSerializer(instance=self.queryset, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response({'detail': 'Empty'}, status=HTTP_200_OK)

    def read_one(self, id: int):
        clock = get_object_or_404(Clock, id=id)
        serializer = ClockOutSerializer(instance=clock)
        return Response(serializer.data, status=HTTP_200_OK)

    def update(self):
        pass

    def delete(self):
        pass
