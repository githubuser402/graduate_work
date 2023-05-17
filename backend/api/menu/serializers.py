from rest_framework import serializers
from .models import (
    Dish,
    Category,
    Order,
    Menu,
    Ingradient,
    Restaurant,
    Payment,
    Table,
    RestaurantGallery,
    User,
    DishImage,
    MeasurementUnit,
    PaymentStatus,
    OrderStatus
)


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class DishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class IngradientSerializer(serializers.ModelSerializer):
    measurement_unit = serializers.ChoiceField(choices=MeasurementUnit.choices())

    class Meta:
        model = Ingradient
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=PaymentStatus.choices())

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    is_staff = serializers.BooleanField(required=False)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        exclude = ['is_active']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class RestaurantSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=True)

    class Meta:
        model = Restaurant
        exclude = ('users',)


class RestaurantGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantGallery
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=OrderStatus.choices())

    class Meta:
        model = Order
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_empty_file=False, use_url=True, read_only=True)
    restaurants = RestaurantSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'