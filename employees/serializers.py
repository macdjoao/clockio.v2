from rest_framework import serializers
from django.contrib.auth.models import User


class EmployeeOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active']
