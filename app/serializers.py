from rest_framework import serializers

from app.models import Employee, Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    # employee = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Subscription
        fields = ('user',)


class EmployeeSerializer(serializers.ModelSerializer):
    # subscriptions = serializers.StringRelatedField(many=True)
    # subscriptions = SubscriptionSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'birthday')


