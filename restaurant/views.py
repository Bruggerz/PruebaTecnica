from django import http
from django.http import response
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from restaurant.models import Restaurant
from restaurant.serializers import Restaurant as rt

# Create your views here.

##
# Función de tipo POST que permite crear nueva data de 
# restaurantes
# #
@api_view(['POST'])
def insertarRestaurant(request):
    if request.method=='POST':
        serializer=rt(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

##
# Función de tipo POST que permite actualizar la información de un restaurant seleccionado#
@api_view(['POST'])
def actualizarRestaurant(request):
    restaurant=Restaurant.objects.get(id=request.data['id'])
    serializer= rt(instance=restaurant,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Informacion actualizada correctamente', status.HTTP_200_OK)

##
# Función POST que permite eliminar mediante id el restaurant seleccionado#
@api_view(['POST'])
def eliminarRestaurant(request):
    restaurant=Restaurant.objects.get(id=request.data['id'])
    restaurant.delete()
    return Response('Informacion eliminada correctamente', status.HTTP_200_OK)

##
# Función de tipo GET que trae todo el contenido de los valores almacenados en la base de datos#
@api_view(['GET'])
def restaurant_list(request):
    if(request.method=='GET'):
        restaurant=Restaurant.objects.all()
        serializer=rt(restaurant,many=True)
        return Response(serializer.data)
    return Response('Datos mostrados correctamente')

##
# Función de tipo POST que permite filtrar los datos mediante el nombre del restaurant, mientras
# contenga parte del contenido#
@api_view(['POST'])
def restaurantFiltrado(request):
    if(request.method=='POST'):
        restaurant=Restaurant.objects.filter(nombre_restaurant__contains=request.data['nombre_restaurant'])
        serializers=rt(restaurant,many=True)
        return Response(serializers.data)
    return Response('Datos mostrados correctamente')
