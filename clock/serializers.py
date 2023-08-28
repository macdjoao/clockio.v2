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


class ClockInSerializer(serializers.Serializer):

    # TODO: Criar um serializer EmployeeIn

    employee_id = serializers.IntegerField(required=True)
    entry_date = serializers.DateTimeField(required=True)
    out_date = serializers.DateTimeField(required=True)
    description = serializers.CharField(required=False)

    def validate(self, data):
        if data['entry_date'] > data['out_date']:
            raise serializers.ValidationError(
                'out_date must occur after entry_date')
        return data

    def create(self, validated_data):
        return Clock.objects.create(**validated_data)
