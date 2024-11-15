from rest_framework.serializers import ModelSerializer
from .models import Product, ProductImage,Order,OrderItem

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'
