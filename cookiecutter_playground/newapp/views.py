from django.http import JsonResponse

from .models import Product
from .serializers import ProductSerializer


def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(
        {
            "data": serializer.data,
        },
    )
