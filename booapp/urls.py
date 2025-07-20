from django.urls import path
from.import views

urlpatterns=[
    path('home',views.product_list,name='product_list'),
    path('',views.register_view,name='register_view'),
    path('login',views.login_view,name='login_view'),
    path('logout',views.logout_view,name='logout_views'),
    path('product/<int:product_id>',views.product_detail,name='product_detail'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart_view,name='cart_view'),
    path('remove_cart/<int:cart_itemid>',views.remove_from_cart,name='remove_from_cart'),
    path('checkout',views.checkout,name='checkout'),
    path('order_success',views.order_success,name='order_success'),
    path('payment',views.verify_payment,name='verify_payment'),
   
]   