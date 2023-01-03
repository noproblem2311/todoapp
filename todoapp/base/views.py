from django.shortcuts import render
from .models    import *
from .serializers import *
from rest_framework.decorators import  api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def getPlan(request):
    plans = Plan.objects.all()
    serializers = PlanSerializer(plans, many = True)
    return Response(serializers.data)

@api_view(['GET'])
def getType(request):
    types = Type.objects.all()
    serializers = TypeSerializer(types, many = True)
    return Response(serializers.data)
    
@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializers = TaskSerializer(tasks, many = True)
    return Response(serializers.data)