from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import BasePermission
from django.db import IntegrityError
import json


from .models import (
    User,
    Restaurant,
    Menu,
    RestaurantGallery,
    Category,
    Dish,
)

from .serializers import (
    UserSerializer,
    RestaurantSerializer,
    MenuSerializer,
    RestaurantGallerySerializer,
    CategorySerializer,
    DishSerializer,
)


def server_error(request):
    return Response({'detail': 'Server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RequireAuthenticationForGet(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' and request.user.is_anonymous:
            return False
        return True


@api_view(["GET", "POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([RequireAuthenticationForGet])
def user_view(request):
    if request.method == "GET":
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        print(request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'detail': 'User exists'})


@api_view(["GET", "POST", 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_view(request):
    try:
        restaurant_id = request.GET.get('id', None)
        if (restaurant_id and (not restaurant_id.isdigit())):
            raise ValueError
    except ValueError:
        return Response({'detail': 'restaurant_id must be integer'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        if restaurant_id:
            try:
                print(request.user)
                restaurant = request.user.restaurants.get(id=restaurant_id)
                serializer = RestaurantSerializer(restaurant)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Restaurant.DoesNotExist:
                return Response({'detail': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

        restaurants = request.user.restaurants.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'detail': 'Not valid data', 'errors': serializer.error_messages}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            # serializer.users.add(request.user)
            restaurant = serializer.save()
            restaurant.users.add(request.user)
            restaurant.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'detail': 'Restaurant exists'}, status=status.HTTP_409_CONFLICT)

    elif request.method == 'DELETE':
        if not restaurant_id:
            return Response({'detail': 'No restaurant_id provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            restaurant = request.user.restaurants.get(id=restaurant_id)
            if request.user in restaurant.users.all():
                restaurant.delete()
                return Response({'detail': 'restaurant deleted'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'detail': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)

        except Restaurant.DoesNotExist:
            return Response({'detail': 'Restaurant does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
@authentication_classes([JWTAuthentication])
def restaurant_gallery_view(request):
    return Response()


@api_view(["GET", "POST", 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
@parser_classes([MultiPartParser, FormParser])
def menu_view(request, restaurant_id):
    try:
        menu_id = request.GET.get('id', None)
        if (menu_id and (not menu_id.isdigit())):
            raise ValueError
    except ValueError:
        return Response({'detail': 'menu_id must be integer'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        restaurant = request.user.restaurants.get(id=restaurant_id)

    except Restaurant.DoesNotExist:
        return Response({'detail': 'no restaurant found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if menu_id:
            try:
                menu = restaurant.menus.get(id=menu_id)
                serializer = MenuSerializer(menu)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Menu.DoesNotExist:
                return Response({'detail': 'menu doesnt exist'}, status=status.HTTP_404_NOT_FOUND)

        menus = restaurant.menus.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # if request.user not in restaurant.users.all():
        #     return Response({'detail': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)

        try:
            json_data = json.loads(request.data.get('json', {}))
        except json.JSONDecodeError:
            return Response({'detail': 'invalid json data'}, status=status.HTTP_400_BAD_REQUEST)

        print(json_data)

        image = request.FILES.get('image', None)
        serializer = MenuSerializer(data=json_data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # menu = serializer.save()
        menu = Menu(**serializer.validated_data)
        menu.restaurant = restaurant

        if image != None:
            menu.image.save(image.name, image)

        menu.save()

        serializer = MenuSerializer(menu)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        if request.user not in restaurant.users.all():
            return Response({'detail': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)

        if not menu_id:
            return Response({'detail': 'no menu_id provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            menu = restaurant.menus.get(id=menu_id)
            menu.delete()
            return Response({'detail': 'menu deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Menu.DoesNotExist:
            return Response({'detail': 'menu does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def menu_category_view(request, restaurant_id, menu_id):
    try:
        restaurant = request.user.restaurants.get(id=restaurant_id)
        menu = restaurant.menus.get(id=menu_id)
    except Restaurant.DoesNotExist:
        return Response({'detail': 'restaurant does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except Menu.DoesNotExist:
        return Response({'detail': 'menu does not exist'}, status=status.HTTP_404_NOT_FOUND)

    try:
        category_id = request.GET.get('id', None)
        if (category_id and (not category_id.isdigit())):
            raise ValueError
    except ValueError:
        return Response({'detail': 'category_id must be integer'}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        if category_id:
            try:
                category = menu.categories.get(id=category_id)
            except Category.DoesNotExist:
                return Response({'detail': 'category does not exist'}, status=status.HTTP_404_NOT_FOUND)

            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            categories = menu.categories.all()
            serialiser = CategorySerializer(categories, many=True)
            return Response(serialiser.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            json_data = json.loads(request.data.get('json', {}))
        except json.JSONDecodeError:
            return Response({'detail': 'invalid json data'}, status=status.HTTP_400_BAD_REQUEST)

        image = request.FILES.get('image', None)
        serializer = CategorySerializer(data=json_data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        category = Category(**serializer.validated_data)

        category.menu = menu

        if image:
            category.image.save(image.name, image)

        category.save()

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if not category_id:
            return Response({'detail': 'no category_id provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            category = menu.categories.get(id=category_id)
            category.delete()
            return Response({'detail': 'category deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Menu.DoesNotExist:
            return Response({'detail': 'category does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def dish_view(request, restaurant_id, menu_id):
    try:
        restaurant = request.user.restaurants.get(id=restaurant_id)
        menu = restaurant.menus.get(id=menu_id)
    except Restaurant.DoesNotExist:
        return Response({'detail': 'restaurant does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except Menu.DoesNotExist:
        return Response({'detail': 'menu does not exist'}, status=status.HTTP_404_NOT_FOUND)

    try:
        dish_id = request.GET.get('id', None)
        if (dish_id and (not dish_id.isdigit())):
            raise ValueError
    except ValueError:
        return Response({'detail': 'dish_id must be integer'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        if dish_id:
            try:
                dish = menu.dishes.get(id=dish_id)
            except Dish.DoesNotExist:
                return Response({'detail': 'dish does not exist'}, status=status.HTTP_404_NOT_FOUND)

            serialiser = DishSerializer(dish)
            return Response(serialiser.data, status=status.HTTP_200_OK)

        dishes = menu.dishes.all()
        serialiser = DishSerializer(dishes, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        if request.user not in restaurant.users.all():
            return Response({'detail': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            json_data = json.loads(request.data.get('json', {}))
        except json.JSONDecodeError:
            return Response({'detail': 'invalid json data'}, status=status.HTTP_400_BAD_REQUEST)
        
        print(request.data)

        serialiser = DishSerializer(data=json_data)

        if not serialiser.is_valid():
            return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

        image = request.FILES.get('image', None)
        # categories_id = set(serialiser.validated_data.pop('categories_id', []))

        try:
            category = menu.categories.get(id=serialiser.validated_data.pop('category_id', None))
        except Category.DoesNotExist:
            return Response({'detail': 'category does not exist'}, status=status.HTTP_404_NOT_FOUND)

        dish = Dish(**serialiser.validated_data)
        dish.menu = menu
        dish.category = category

        if image:
            dish.image.save(image.name, image)

        # categories_to_add = menu.categories.filter(id__in=list(set(category[0] for category in menu.categories.values_list('id')) & categories_id))
        # print('\n\nCategories to add: ', categories_to_add, '\n')

        dish.save()
        serialiser = DishSerializer(dish)
        return Response(serialiser.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        if request.user not in restaurant.users.all():
            return Response({'detail': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)
        
        if not dish_id:
            return Response({'detail': 'dish_id is not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            dish = menu.dishes.get(id=dish_id)
            dish.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Dish.DoesNotExist:
            return Response({'detail': 'dish does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def dish_image_view(request, restaurant_id, menu_id, dish_id):
    return Response()


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def ingradient_view(request, restaurant_id):
    return Response()


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def table_view(request, restaurant_id):
    return Response()
