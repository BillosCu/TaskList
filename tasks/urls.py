from django.urls import path
from .views import ListTask, createTask, deleteTask, updateTask, update

urlpatterns = [
    path('', ListTask),
    path('new/', createTask, name='createTask'),
    path('delete/<int:id>/', deleteTask, name='deleteTask'),
    path('update/<int:id>/', updateTask, name='updateTask'),
    path('update/', update, name='update')
]