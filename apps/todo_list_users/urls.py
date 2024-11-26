from django.urls import path
from .views import UserRegistrationView, TodoListCreateView, TodoDetailView, TodoDeleteAllView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/delete_all/', TodoDeleteAllView.as_view(), name='todo-delete-all'),
]
