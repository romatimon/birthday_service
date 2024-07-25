from django.urls import path, include

from app import views
from app.views import subscribe, unsubscribe

# router = DefaultRouter()
# router.register('employees', EmployeeViewSet, basename='employees')
# router.register('subscription', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('employees/', views.employee_list, name='employees'),
    path('subscribe/<int:employee_id>/', subscribe, name='subscribe'),
    path('unsubscribe/<int:employee_id>/', unsubscribe, name='unsubscribe'),
    path('auth/', include('djoser.urls')),
    path('auth/jwt/', include('djoser.urls.jwt')),
    # path('', include(router.urls)),
    # path('employees/', EmployeeList.as_view()),
    # path('employees/<int:pk>/', EmployeeDetail.as_view())
    # path('employees/', APIEmployee.as_view()),
    # path('employees/<int:pk>/', views.employee_detail)

]
