from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Employee, Subscription
from app.serializers import EmployeeSerializer


@api_view(['GET'])
def employee_list(request):
    """Возвращает список всех сотрудников."""
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def subscribe(request, employee_id):
    """Подписывает пользователя на уведомления о сотруднике."""
    employee = Employee.objects.get(id=employee_id)
    subscription, created = Subscription.objects.get_or_create(user=request.user, employee=employee)

    if created:
        return Response({'message': 'Вы успешно подписаны на уведомления.'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Вы уже подписаны на данного сотрудника!'}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def unsubscribe(request, employee_id):
    """Отписывает пользователя от уведомлений о сотруднике."""
    try:
        subscription = Subscription.objects.get(user=request.user, employee_id=employee_id)
        subscription.delete()
        return Response({'message': 'Вы успешно отписались от уведомлений!'}, status=status.HTTP_204_NO_CONTENT)
    except Subscription.DoesNotExist:
        return Response({'message': 'Подписка отсутствует!'}, status=status.HTTP_404_NOT_FOUND)
