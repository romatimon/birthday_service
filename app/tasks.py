from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Employee, Subscription


@shared_task
def send_birthday_notifications():
    today = timezone.now().date()
    tomorrow = today + timezone.timedelta(days=1)

    employees = Employee.objects.filter(birthday__month=tomorrow.month, birthday__day=tomorrow.day)

    for employee in employees:
        send_mail(
            'Напоминание о дне рождения',
            f'Завтра день рождения у {employee.name}!',
            'from@example.com',
            [employee.email],
            fail_silently=False,
        )