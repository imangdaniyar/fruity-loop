import json

from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer
from core.models import User


class UserDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist as e:
            raise Http404

    def get(self, request, id=None):
        user = self.get_object(id=id)
        user = UserSerializer(user)
        return JsonResponse(user.data)

    def put(self, request, id=None):
        user = self.get_object(id)
        user = UserSerializer(instance=user, data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors)

    def delete(self, request, id=None):
        user = self.get_object(id)
        user.delete()
        return Response({'message': 'deleted'}, status=204)


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users1 = UserSerializer(users, many=True)
        return JsonResponse(users1.data, safe=False)

    def post(self, request):
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
