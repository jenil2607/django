from django.urls import path

from .views import viewCart, addToCart, RemFromCart, addQuantity, remQuantity


urlpatterns = [
    path('cart/', viewCart, name = 'view_cart'),
    path('cart/add/<int:product_id>', addToCart, name = 'add_to_cart' ),
    path('cart/rem/<int:cart_item_id>', RemFromCart, name = 'rem_from_cart'),
         # The following url patterns will be requested by the JS function
    path('cart/add/<int:cart_item_id>/', addQuantity, name='add_quantity'),
    path('cart/remove/<int:cart_item_id>/', remQuantity, name='rem_quantity'),
]