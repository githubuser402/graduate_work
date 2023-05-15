from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 

from .models import User
from .serializers import UserSerializer

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user_view(request):
    if request.method == "GET":
        user_id = request.GET.get('user_id')
        if user_id is not None:
            try:
                user = User.objects.get(id=user_id)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
             
    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserTokenObtainPairView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         print("this called")
#         response = super().post(request, *args, **kwargs)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = User.objects.get(username=serializer.validated_data['username'])
#         user_serializer = UserSerializer(user)
#         token = RefreshToken.for_user(user)

#         response.data['user'] = user_serializer.data
#         response.data['access_token'] = str(token.access_token)
#         response.data['refresh_token'] = str(token)

#         return response


# class UserTokenRefreshView(TokenRefreshView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = User.objects.get(username=serializer.validated_data['username'])
#         user_serializer = UserSerializer(user)

#         response.data['user'] = user_serializer.data

#         return response
