from django.contrib import admin
from.models import product,CartItem,Order



# Register your models here.
@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','created_at')
    search_fields=('name',)
    list_filter=('created_at',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display=('user','product','quantity','added_at')
    list_filter=('added_at',)
    search_fields=('user__username','product__name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','user','name','phone','email','total_price','status','ordered_at')
    list_filter=('status','ordered_at')
    search_fields=('user__username',)
    filter_horizontal=('items',)
