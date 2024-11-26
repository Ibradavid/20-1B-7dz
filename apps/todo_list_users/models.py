from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(regex=r'^\+996\d{9}$', message='Номер телефона должен быть в тком формате: +996XXXXXXXXX')]
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions',
        blank=True
    )


class Todo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='todo_list_images/', null=True, blank=True)

    def __str__(self):
        return self.title
