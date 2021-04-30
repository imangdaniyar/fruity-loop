from rest_framework import serializers

from core.models import Product, Storage


class ProductSerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.price = validated_data['price']
        instance.quantity = validated_data['quantity']
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity')


class StorageSearializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    productId = serializers.IntegerField()
    quantity = serializers.IntegerField
    address = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Storage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
