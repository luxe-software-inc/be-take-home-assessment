from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from movies.views.customers_view import CustomerViewSet
from movies.views.movie_view import MovieViewSet
from movies.views.wishlist_view import WishlistViewSet

router = DefaultRouter()
router.register(
    r'customers',
    CustomerViewSet,
)
router.register(
    r'movie',
    MovieViewSet,
)
router.register(
    r'wishlist',
    WishlistViewSet,
)

app_name = 'movies'

urlpatterns = [
    path('', include(router.urls))
]
