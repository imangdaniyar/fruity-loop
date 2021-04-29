from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from core.models import User, Product, Order, Storage


@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_json = [user.to_json() for user in users]
        return JsonResponse(users_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.create(
                name=data['name'],
                surname=data['surname'],
                email=data['email'],
                password=data['password'],
                address=data['address']
            )
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
        return JsonResponse(user.to_json(), status=200)


@csrf_exempt
def user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(user.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        user.name = data['name']
        user.save()
        return JsonResponse(user.to_json())
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'deleted'}, status=204)