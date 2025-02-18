from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from cookiecutter_playground.newapp import views
from cookiecutter_playground.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("products/", view=views.product_list),
    path("products/info/", view=views.product_info),
    path("products/<int:pk>", view=views.product_detail),
    path("orders/", view=views.order_list),
]

app_name = "api"
urlpatterns + router.urls
