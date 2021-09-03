from rest_framework import serializers
from Ecom.models import Orders,Mycart,Items

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=["product","address"]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mycart
        fields='__all__'

class AddToCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = ('id',)

