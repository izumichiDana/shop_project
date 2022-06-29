from .models import *
from django.contrib import admin
from django.contrib.admin import StackedInline, TabularInline
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin


class Product_to_OrderInline(SuperInlineModelAdmin, TabularInline):
    model = OrderProduct
    extra = 0
    readonly_fields = ('byer', 'image', 'color', 'name', 'size', 'old_price', 'price', 'count')
    list_display = ('byer', 'image', 'color', 'name', 'size', 'old_price', 'price', 'count')
    fields = ('byer', 'image', 'color', 'name', 'size', 'old_price', 'price', 'count')

    can_delete = False


class OrderInline(SuperInlineModelAdmin, StackedInline):
    model = Order
    inlines = (Product_to_OrderInline,)
    extra = 0
    readonly_fields = ('byer', 'stock', 'quantity', 'price', 'sale', 'final_price')

    can_delete = False


class ByerAdmin(SuperModelAdmin):
    model = Byer
    inlines = [OrderInline]
    list_filter = ['choise', 'email']
    fields = ('name', 'last_name', 'city', 'email', 'country', 'choise', 'created_at')
    list_display = ('name', 'last_name', 'city', 'email', 'country', 'choise', 'created_at' )
    readonly_fields = ('created_at', )

    def get_total_price(self, obj):
        order_check = Order.objects.get(client=obj)
        return order_check.final_price




admin.site.register(Byer, ByerAdmin)





