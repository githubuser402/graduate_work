from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from menu.management.commands.bot import send_order_message

from menu.models import (
    Restaurant,
    Menu,
    Category
)

from .serializers import (
    MenuSerializer,
    CategorySerializer,
    OrderDishSerializer,
    OrderSerializer,
)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def menu_view(request, restaurant_id, menu_id):
    if request.method == 'GET':
        try: 
            # restaurant = Restaurant.objects.get(id=restaurant_id)
            menu = Menu.objects.filter(restaurant__id=restaurant_id).get(id=menu_id)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        print(menu)
        
        return Response(MenuSerializer(menu).data)
        

        
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def category_view(request, restaurant_id, menu_id, category_id):
    if request.method == 'GET':
        try: 
            category = Category.objects.filter(menu__restaurant__id=restaurant_id).filter(menu__id=menu_id).get(id=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
                    
        return Response(CategorySerializer(category).data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def order_view(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            restaurant = Restaurant.objects.get(id=serializer.validated_data['restaurant_id'])
            user = restaurant.users.first()
        except Restaurant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        print(serializer.validated_data)

        try:
            send_order_message(user, serializer.validated_data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

        
        