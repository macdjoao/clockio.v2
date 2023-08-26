from rest_framework import serializers
from clock.models import Clock
# from django.contrib.auth.models import User
from employees.serializers import EmployeeOutSerializer


class ClockOutSerializer(serializers.ModelSerializer):
    employee = EmployeeOutSerializer()

    class Meta:
        model = Clock
        fields = ['id',
                  'entry_date',
                  'out_date',
                  'description',
                  'to_correction',
                  'employee',
                  'updated_at',
                  'created_at']


# class ClockOutSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     # employee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     employee = EmployeeOutSerializer()
#     entry_date = serializers.DateTimeField()
#     out_date = serializers.DateTimeField()
#     description = serializers.CharField(max_length=255)
#     to_correction = serializers.BooleanField()
