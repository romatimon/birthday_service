from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    """Модель сотрудника."""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.name


class Subscription(models.Model):
    """Модель подписок."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='subscriptions')

    def __str__(self):
        return f"{self.user.username} подписан на {self.employee.name}"
