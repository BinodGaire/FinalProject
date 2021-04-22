from django.contrib import admin
from django.urls import path, include
from salesapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),

    # path('load/', views.load_data, name='load_data'),

    # each product category page
    path('health-beauty/', views.health_beauty, name='health_beauty'),
    path('home-lifestyle/', views.home_lifestyle, name='home_lifestyle'),
    path('sports-travel/', views.sports_travel, name='sports_travel'),
    path('electronic-accessories/', views.electronic_accessories,
         name='electronic_accessories'),
    path('fashion-accessories/', views.fashion_accessories,
         name='fashion_accessories'),
    path('food-beverages/', views.food_beverages, name='food_beverages'),
]
