from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from enumfields import Enum, EnumField
from django.db.models.signals import pre_delete
from django.dispatch import receiver

    

class MeasurementUnit(Enum):
    KILOGRAMS = 'kg'
    GRAMS = 'g'
    LITERS = 'l'
    MILLILITERS = 'ml'
    PIECES = 'pieces'
    PACKS = 'packs'

    
class PaymentStatus(Enum):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'
    REFUNDED = 'Refunded'


class Payment(models.Model):
    time = models.DateTimeField(auto_now=True)
    status = EnumField(PaymentStatus, default=PaymentStatus.PENDING) 
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"payment {self.id} {self.status}"


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=70, null=True)
    description = models.TextField(default='')
    contact_number = models.JSONField(default=dict)
    email = models.JSONField(default=dict)
    users = models.ManyToManyField(User, related_name="restaurants")

    def __str__(self):
        return self.name
    

class RestaurantGallery(models.Model):
    image = models.ImageField(upload_to="restaurant_gallery")
    restaurant = models.ForeignKey(Restaurant, related_name="gallery", on_delete=models.CASCADE)

    def __str__(self):
        return f"restaurant image {self.id}"


class Table(models.Model):
    name = models.CharField(max_length=30)
    restaurant = models.ForeignKey(Restaurant, related_name="tables", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class OrderStatus(Enum):
    COOKING = 'Cooking'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'


class Menu(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to="menu_backgrounds", null=True)
    restaurant = models.ForeignKey(Restaurant, related_name='menus', on_delete=models.CASCADE)
    # categories = models.ManyToManyField(Category, related_name='menus')
    # dishes = models.ManyToManyField(Dish, related_name='menus')
    
    def __str__(self):
        return self.title
    


class Dish(models.Model):
    image = models.ImageField(upload_to="dish_images")
    name = models.CharField(max_length=60)
    description = models.TextField()
    recipe = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    menu = models.ForeignKey(Menu, related_name="dishes", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"
    

class DishImage(models.Model):
    dish = models.ForeignKey(Dish, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="dish_images")
    
    def __str__(self):
        return f"dish image {self.id}"
    

class Category(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to="category_images")
    dishes = models.ManyToManyField(Dish, related_name="categories")
    created_at = models.DateTimeField(auto_now=True)
    menu = models.ForeignKey(Menu, related_name="categories", on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.title}"
    

class Ingradient(models.Model):
    name = models.CharField(max_length=60)
    measurement_unit = EnumField(MeasurementUnit, default=MeasurementUnit.KILOGRAMS)
    available_count = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=60)
    dish = models.ForeignKey(Dish, related_name="ingradients", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    time = models.DateTimeField(auto_created=True)
    status = EnumField(OrderStatus, default=OrderStatus.COOKING)
    dishes = models.ManyToManyField(Dish, related_name="orders")
    user = models.ForeignKey(User, related_name="orders", on_delete=models.DO_NOTHING)
    table = models.ForeignKey(Table, related_name="tables",on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"order {self.id} {self.status}"