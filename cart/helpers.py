from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart:
    def __init__(self, request):
        """Инициализация корзины(сессии)
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add_or_update(self, product, quantity=1, update_quantity=False ):
        """Добавить в корзину либо обновить его количество
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {

                                    'product': str(product.id),
                                    'stock': str(product.stock),
                                    'old_price': str(product.old_price),
                                    'new_price': str(product.price),
                                    'price': str(product.price),
                                    'quantity': 0,
                                    # 'colors':str(color)
                                    }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity


        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def remove(self, product, minus):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        """Перебор элементов в корзине,
        также получим необходимые продукты в бд
        """
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        """Подчет всех товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        """Подчет стоймости товаров в корзине
        """

        return {"price": sum(Decimal(item['old_price']) * item['quantity'] for item in self.cart.values()),
                "sale": sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()),
                # "line_quantity": sum(int(item['stock']) * item['stock'] for item in self.cart.values())
                 }
   
    def get_total_quantity(self):
        """
        Подсчет всех товаров из корзины (штук)
        """
        return sum(int(item['stock']) * item['quantity'] for item in self.cart.values())
        
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

