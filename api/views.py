from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DriverSerializer
from .models import Driver


# Create your views here.
@api_view(['GET'])
def driverdetail(request,pk):
    driver = Driver.objects.get(id=pk)
    serializer = DriverSerializer(driver, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createdriver(request):
    serializer = DriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatedriver(request,pk):
    driver = Driver.objects.get(id=pk)
    serializer = DriverSerializer(instance=driver,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletedriver(request,pk):
    driver = Driver.objects.get(id=pk)
    driver.delete()
    return Response('Deleted successfully')