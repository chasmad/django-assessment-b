from django.urls import path
from .views import index, delete, CreateItem


urlpatterns = [
    path('', index),
    path('add/', CreateItem.as_view(), name='add_item'),
    path('delete/<int:id>', delete, name='delete_item'),
]