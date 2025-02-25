from django.urls import path

from .views import viewCart, addToCart


urlpatterns = [
    path('cart/', viewCart, name = 'view_cart'),
    path('cart/add/<int:product_id>', addToCart, name = 'add_to_cart' )
]