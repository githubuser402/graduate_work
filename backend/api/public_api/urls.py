from django.urls import path
from . import views


urlpatterns = [
    path('r/<int:restaurant_id>/m/<int:menu_id>/', views.menu_view, name='menu_view'),
    path('r/<int:restaurant_id>/m/<int:menu_id>/c/<int:category_id>/', views.category_view, name='category_view'),
]