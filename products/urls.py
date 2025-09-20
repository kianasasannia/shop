from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('product/<int:id>/',views.product_detail,name="product_detail"),
    path('category/<int:category_id>/',views.products_by_category,name="products_by_category"),
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name="add-to-cart"),
    path('cart/',views.cart_view,name="cart_view"),
    path('cart/decrease/<int:product_id>/',views.decrease_quantity,name="decrease_quantity")
]
