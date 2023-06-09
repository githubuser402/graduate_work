from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from menu.models import (
    Menu,
)

from .serializers import (
    MenuSerializer,
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
        

        
