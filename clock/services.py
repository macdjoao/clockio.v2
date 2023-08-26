from clock.models import Clock
from clock.serializers import ClockOutSerializer
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response


class ClockService:
    def __init__(self) -> None:
        self.queryset = Clock.objects.all()

    def create(self):
        pass

    def read_list(self):
        if self.queryset:
            serializer = ClockOutSerializer(instance=self.queryset, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response({'detail': 'Empty'}, status=HTTP_200_OK)

    def read_one(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
