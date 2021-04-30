from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from api.views import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('users/<int:id>', views.UserDetailAPIView.as_view(), name='userDetail'),
    path('users', views.UserListAPIView.as_view(), name='userList'),
    path('storage/<int:id>', views.storages),
    path('products/', views.product_list),
    path('products/<int:pk>', views.ProductDetailAPIView.as_view(), name='userDetail'),
]
