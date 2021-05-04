from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_nav, name='api_nav'),
    path('add-supplies/', views.add_supplies, name='add_supplies'),
    path('view-supplies/', views.view_supplies, name='view_supplies'),
    path('update-supplies/<int:pk>', views.update_supplies, name='update_supplies'),
    path('delete-supplies/<int:pk>', views.delete_supplies, name='delete_supplies'),
]