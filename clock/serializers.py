from rest_framework import serializers
from django.contrib.auth.models import User
from clock.models import Clock
from employees.serializers import EmployeeOutSerializer


# class ClockOutSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Clock
#         fields = '__all__'
#         depth = 1


class ClockOutSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    # employee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    employee = EmployeeOutSerializer()
    entry_date = serializers.DateTimeField()
    out_date = serializers.DateTimeField()
    description = serializers.CharField(max_length=255)
    to_correction = serializers.BooleanField()
