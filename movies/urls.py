from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from movies.views.customers_view import CustomerViewSet

router = DefaultRouter()
router.register(
    r'customers',
    CustomerViewSet,
)

app_name = 'movies'

urlpatterns = [
    path('', include(router.urls))
]
