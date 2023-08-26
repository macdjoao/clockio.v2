from rest_framework import serializers
from clock.models import Clock
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
