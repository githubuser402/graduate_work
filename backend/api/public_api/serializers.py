from rest_framework import serializers
from menu.models import (
    Dish,
    Category,
    Menu,
    Restaurant,
)

class DishSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=255)
    recipe = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'recipe', 'price', 'image')

class RestaurantSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    contact_number = serializers.JSONField()
    email = serializers.JSONField()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'description', 'contact_number', 'email', 'categories')


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60)
    image = serializers.ImageField(read_only=True)
    created_at = serializers.DateTimeField()
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'created_at', 'dishes')


class CategoryGeneralSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60)
    image = serializers.ImageField(read_only=True)
    created_at = serializers.DateTimeField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'created_at')


class MenuSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60)
    image = serializers.ImageField(read_only=True)
    categories = CategoryGeneralSerializer(many=True, read_only=True)
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = ('id', 'title', 'image', 'categories', 'restaurant')


class OrderDishSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.Serializer):
    time = serializers.DateTimeField()
    dishes = OrderDishSerializer(many=True)
    table_number = serializers.IntegerField()
    restaurant_id = serializers.IntegerField()
    menu_id = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)