from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Employee, Subscription
from app.serializers import EmployeeSerializer, SubscriptionSerializer

from rest_framework import generics


# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def subscribe(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    subscription, created = Subscription.objects.get_or_create(user=request.user, employee=employee)

    if created:
        return Response({'message': 'Вы успешно подписаны на уведомления.'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Вы уже подписаны на данного сотрудника!'}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def unsubscribe(request, employee_id):
    try:
        subscription = Subscription.objects.get(user=request.user, employee_id=employee_id)
        subscription.delete()
        return Response({'message': 'Вы успешно отписались от уведомлений!'}, status=status.HTTP_204_NO_CONTENT)
    except Subscription.DoesNotExist:
        return Response({'message': 'Подписка отсутствует!'}, status=status.HTTP_404_NOT_FOUND)


# class SubscriptionViewSet(viewsets.ModelViewSet):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionSerializer


# class EmployeeList(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#
# class EmployeeDetail(generics.RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class APIEmployee(APIView):
#     def get(self, request):
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def employee_list(request):
#     if request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     employees = Employee.objects.all()
#     serializer = EmployeeSerializer(employees, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def employee_detail(request, pk):
#     employee = Employee.objects.get(id=pk)
#     if request.method == 'PUT' or request.method == 'PATCH':
#         serializer = EmployeeSerializer(employee, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     serializer = EmployeeSerializer(employee)
#     return Response(serializer.data)


