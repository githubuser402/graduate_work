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


class DishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishImage
        fields = '__all__'


class DishSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)
    description = serializers.CharField()
    recipe = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    categories_id = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    images = DishImageSerializer(many=True, read_only=True)
    image = serializers.ImageField(read_only=True)

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)  # Retrieve the 'fields' argument
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())

            for field_name in existing - allowed:
                self.fields.pop(field_name)


    def create(self, validated_data):
        categories_id = validated_data.pop('categories_id', [])
        dish = Dish.objects.create(**validated_data)

        # Add categories to the dish
        # dish.categories.set(categories_id)
        return dish

    def update(self, instance, validated_data):
        categories_id = validated_data.pop('categories_id', [])
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.recipe = validated_data.get('recipe', instance.recipe)
        instance.price = validated_data.get('price', instance.price)

        # Update categories of the dish
        # instance.categories.set(categories_id)
        instance.save()
        return instance
    

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60)
    image = serializers.ImageField(read_only=True)
    dishes = DishSerializer(many=True, read_only=True, fields=['id', 'name', 'price'])
    created_at = serializers.DateTimeField(read_only=True)

    
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)  # Retrieve the 'fields' argument
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())

            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    

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
    # categories = CategorySerializer(many=True, read_only=True, fields=['id', 'title', 'image', 'created_at'])
    # dishes = DishSerializer(many=True, read_only=True) 

    class Meta:
        model = Menu
        # fields = '__all__'
        exclude = ('restaurant',)