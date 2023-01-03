from .models import *
from rest_framework import serializers

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    Plan = PlanSerializer(many = False, required=False)
    class Meta:
        model = Type
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    Type = TypeSerializer(many = False, required=False)
    class Meta:
        model = Task
        fields = '__all__'
