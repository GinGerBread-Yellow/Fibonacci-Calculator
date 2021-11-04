from rest_framework import serializers
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(default=1)

    class Meta:
        model = OrderItem
        fields = ('__all__')