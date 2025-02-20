from django.urls import path

from .views import homeView, aboutView, AddProduct, ProductDetails, UpdateProduct, DeleteProduct, searchView

urlpatterns = [
    path("", homeView, name="homepage"),
    path("about", aboutView, name="aboutpage"),
    
    path("products/add",           AddProduct.as_view(),      name = "addproduct"),     # C
    path("Products/int<pk>",       ProductDetails.as_view(),  name = "prod_details"),   # R
    path("Products/edit/<int:pk>", UpdateProduct.as_view(),   name = "editproduct"),    # u
    path("Products/del/<int:pk>",  DeleteProduct.as_view(),   name = "delproduct"),     # D

    # search parh
    path('products/search', searchView, name = 'search')    
] 
