from django.contrib import admin

from .models import *

class ByerAdmin(admin.ModelAdmin):
    fields = ('name', 'last_name', 'city', 'email', 'country', 'choise', 'created_at')
    list_display = ('name', 'last_name', 'city', 'email', 'country', 'choise', 'created_at' )
    readonly_fields = ('created_at', )


class OrderAdmin(admin.ModelAdmin):
    fields = ('byer', 'stock', 'quantity', 'price', 'sale', 'final_price')
    list_display = ('byer', 'stock', 'quantity', 'price', 'sale', 'final_price')
    readonly_fields = ('byer', 'stock', 'quantity', 'price', 'sale', 'final_price')


class OrderProductAdmin(admin.ModelAdmin):
    fields = ('byer', 'image', 'color', 'name', 'size', 'old_price', 'price', 'count')
    list_display = ('byer', 'image', 'color', 'name', 'size', 'old_price', 'price', 'count')
    readonly_fields = ('byer', 'image', 'color', 'name', 'size', 'old_price', 'price', 'count')



admin.site.register(Byer, ByerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)







