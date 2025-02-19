from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from cookiecutter_playground.newapp import views
from cookiecutter_playground.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("products/", view=views.ProductListAPIView.as_view()),
    path("products/info/", view=views.product_info),
    path("products/<int:product_id>/", view=views.ProductDetailAPIView.as_view()),
    path("orders/", view=views.OrderListAPIView.as_view()),
]

app_name = "api"
urlpatterns + router.urls
