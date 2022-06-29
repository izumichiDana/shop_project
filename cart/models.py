from django.db import models
from products.models import Product
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from colorfield.fields import ColorField
from django.db import models
from datetime import datetime

BYER_LIST = (
    ('New', 'Новый'),
    ('Ordered', 'Оформлен'),
    ('Deleted', 'Отменен'),
)

class Byer(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    phone_num = PhoneNumberField(blank=True, verbose_name='Номер')
    city = models.CharField(max_length=100, verbose_name='Страна')
    country = models.CharField(max_length=100, verbose_name='Город')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления')
    choise  = models.CharField(choices=BYER_LIST, max_length=50, verbose_name='Выбор из списка', default='Новый')

    class Meta:
        verbose_name = 'Информация юзера'
        verbose_name_plural = 'Информация юзера'

    def __str__(self):
        return f'{self.name} {self.last_name} {self.city} {self.email} {self.country} {self.choise} {self.created_at}'


class Order(models.Model):
    byer = models.ForeignKey(Byer,
                               on_delete=models.CASCADE,
                               related_name='byer',
                               )
    quantity = models.IntegerField(verbose_name='Количество линеек')
    stock = models.IntegerField(verbose_name='Количество товара')
    price = models.FloatField(verbose_name='Сумма')
    sale = models.FloatField(verbose_name='Скидка')
    final_price = models.FloatField(verbose_name='Итого к оплате')

    def __str__(self):
        return str(self.id)

    def get_final_price(self):
        return self.final_price

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'



class OrderProduct(models.Model):
    byer = models.ForeignKey(Order,
                               on_delete=models.CASCADE,
                               related_name='order',
                               )
    image = models.ImageField(verbose_name='Фотография', blank=True, null=True,)
    color = ColorField(default=True, verbose_name='Цвет')
    name = models.CharField(max_length=255, verbose_name='Название')
    size = models.CharField(max_length=20, verbose_name='Размерный ряд')
    old_price = models.IntegerField(verbose_name='Цена')
    price = models.FloatField(verbose_name='Цена после скидки')
    count = models.IntegerField(verbose_name='Количество товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Детализация заказа'
        verbose_name_plural = 'Детализация заказа'

