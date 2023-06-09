from django.urls import path
from . import views


urlpatterns = [
    path('r/<int:restaurant_id>/m/<int:menu_id>/', views.menu_view, name='menu_view'),
]