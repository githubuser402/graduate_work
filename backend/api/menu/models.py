from django.db import models
from enumfields import Enum, EnumField


class Dish(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    recipe = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    

class DishImage(models.Model):
    dish = models.ForeignKey(Dish, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="dish_images")

    def __str__(self):
        return f"dish image {self.id}"
    

class Category(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    image = models.ImageField(upload_to="category_images")
    dish = models.ForeignKey(Dish, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    

class MeasurementUnit(Enum):
    KILOGRAMS = 'kg'
    GRAMS = 'g'
    LITERS = 'l'
    MILLILITERS = 'ml'
    PIECES = 'pieces'
    PACKS = 'packs'


class Ingradient(models.Model):
    name = models.CharField(max_length=60)
    measurement_unit = EnumField(MeasurementUnit, default=MeasurementUnit.KILOGRAMS)
    available_count = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    dish = models.ForeignKey(Dish, related_name="ingradients", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
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


class User(models.Model):
    username = models.CharField() 
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False) 
    email = models.EmailField()
    slug = models.SlugField()

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=70)
    description = models.TextField()
    contact_number = models.JSONField()
    email = models.JSONField()
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
    link = models.SlugField()
    restaurant = models.ForeignKey(Restaurant, related_name="tables", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class OrderStatus(Enum):
    COOKING = 'Cooking'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'


class Order(models.Model):
    time = models.DateTimeField(auto_created=True)
    status = EnumField(OrderStatus, default=OrderStatus.COOKING)
    dishes = models.ManyToManyField(Dish, related_name="orders")
    user = models.ForeignKey(User, related_name="orders", on_delete=models.DO_NOTHING)
    table = models.ForeignKey(Table, related_name="tables",on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"order {self.id} {self.status}"


class Menu(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to="menu_backgrounds")
    slug = models.SlugField()

    def __str__(self):
        return self.title