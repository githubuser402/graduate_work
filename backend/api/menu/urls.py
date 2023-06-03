from django.urls import path
from .views import (
    user_view,
    restaurant_view,
    restaurant_gallery_view,
    table_view,
    menu_view,
    dish_view,
    menu_category_view,
    ingradient_view,
    dish_image_view,
    server_error
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)

handler500 = server_error

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('u/', user_view, name='user'),
    path('r/', restaurant_view, name='restaurant_view'),
    path('r/<int:restaurant_id>/g/', restaurant_gallery_view, name='restaurant_gallery_view'),
    path('r/<int:restaurant_id>/t/', table_view, name='restaurant_table_view'),
    path('r/<int:restaurant_id>/m/', menu_view, name='restaurant_menu_view'),
    path('r/<int:restaurant_id>/m/<int:menu_id>/d/', dish_view, name='restaurant_dish_view'),
    path('r/<int:restaurant_id>/m/<int:menu_id>/d/<int:dish_id>/i/', dish_image_view, name='restaurant_dish_image_view'),
    path('r/<int:restaurant_id>/m/<int:menu_id>/c/', menu_category_view, name='restaurant_menu_category_view'),
    path('r/<int:restaurant_id>/i/', ingradient_view, name='restaurant_ingradient_view'),
]
