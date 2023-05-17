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
    Menu
)

from .serializers import (
    UserSerializer,
    RestaurantSerializer,
    MenuSerializer,
)


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
    restaurant_id = request.GET.get('restaurant_id', None)
    if request.method == 'GET':
        if restaurant_id:
            try:
                restaurant = Restaurant.objects.get(id=restaurant_id)
                serializer = RestaurantSerializer(restaurant)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Restaurant.DoesNotExist:
                return Response({'detail': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'detail': 'Not valid data', 'errors': serializer.error_messages}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            serializer.users.add(request.user)
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'detail': 'Restaurant exists'}, status=status.HTTP_409_CONFLICT)

    elif request.method == 'DELETE':
        if not restaurant_id:
            return Response({'detail': 'No restaurant_id provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            if request.user in restaurant.users.all():
                restaurant.delete()
                return Response({'detail': 'restaurant deleted'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'detail': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)

        except Restaurant.DoesNotExist:
            return Response({'detail': 'Restaurant does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def restaurant_gallery_view(request):
    return Response()


@api_view(["GET", "POST", 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
@parser_classes([MultiPartParser, FormParser])
def menu_view(request, restaurant_id):
    menu_id = request.GET.get('menu_id', None)

    try:
        restaurant = Restaurant.objects.get(id=restaurant_id)
        if request.user not in restaurant.users.all():
            return Response({'detail': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)

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
        try:
            json_data = json.loads(request.data.get('json', {}))
        except json.JSONDecodeError:
            return Response({'detail': 'invalid json data'}, status=status.HTTP_400_BAD_REQUEST)
        
        image = request.FILES.get('image', None)
        serializer = MenuSerializer(data=json_data)
        if serializer.is_valid():
            menu = serializer.save()
            menu.restaurants.add(restaurant)
            
            if image != None:
                menu.image.save(image.name, image)

            menu.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            menu = restaurant.menus.get(id=menu_id)
            menu.delete()
            return Response({'detail': 'menu deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Menu.DoesNotExist:
            return Response({'detail': 'menu does not exist'}, status=status.HTTP_404_NOT_FOUND)
        

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def menu_category_view(request, restaurant_id, menu_id):
    return Response()


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def dish_view(request, restaurant_id, menu_id):
    return Response()


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
