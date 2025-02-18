from rest_framework import serializers

from .models import Order
from .models import OrderItem
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "stock",
        )

    def validate_price(self, value):
        if value <= 0:
            msg = "price must be greater than 0"
            raise serializers.ValidationError(msg)
        return value
