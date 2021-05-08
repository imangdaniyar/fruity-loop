from rest_framework.decorators import api_view

from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse

from rest_framework.request import Request
from rest_framework.response import Response

from core.models import Storage
from api.serializers import StorageSerializer, StorageSerializer2, OrderSerializer2


@api_view(['GET', 'POST'])
def storage_list(request):
    if request.method == 'POST':
        serializer = StorageSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'GET':
        storages = Storage.objects.all()
        serializer = StorageSerializer2(storages, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def storage_detail(request, id):
    try:
        storage = Storage.objects.get(id=id)
    except Storage.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)
    if request.method == 'GET':
        serializer = StorageSerializer2(storage)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StorageSerializer(instance=storage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        storage.delete()
        return Response({'message': 'deleted'}, status=204)

@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'POST':
        serializer = OrderSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'GET':
        orders = Storage.objects.all()
        serializer = OrderSerializer2(orders, many=True)
        return Response(serializer.data)
