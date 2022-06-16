from django.db import models
from colorfield.fields import ColorField

class Collections(models.Model):
    name = models.CharField(max_length=100, verbose_name='Коллекция')
    slug =models.SlugField(max_length=100, unique=True)
    images = models.ImageField(upload_to='collction_image')

    class Meta:
        ordering = ('name', )
        verbose_name = ' Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    slug =models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    collection = models.ForeignKey(Collections, related_name='products', 
                                                on_delete=models.CASCADE, 
                                                blank=True, null=True, 
                                                verbose_name='Коллекция')
    category = models.ForeignKey(Category, related_name='products', 
                                           on_delete=models.CASCADE, 
                                           verbose_name='Категоря' )
    top_saled = models.BooleanField(default=True, verbose_name='Хит продаж')
    new_product = models.BooleanField(default=True, verbose_name='Новинки')
    name = models.CharField(max_length=100, verbose_name='название')
    slug = models.SlugField(max_length=100, unique=True)
    vendor_code = models.CharField(max_length=100, verbose_name='артикул')
    old_price = models.IntegerField(default=True, verbose_name='старая цена')
    sale = models.IntegerField(default=True,  verbose_name='скидка')
    price = models.IntegerField(default=True, verbose_name='Цена', blank=True, null=True )
    description = models.TextField(verbose_name='описание')
    size = models.CharField(max_length=100, verbose_name='Размер')
    count = models.IntegerField(default=True, verbose_name='Количество линеек',)
    stock = models.IntegerField(default=True, verbose_name='Количество в линейке', blank=True, null=True)
    sostav = models.CharField(max_length=100, verbose_name='Состав')
    material = models.CharField(max_length=100, verbose_name='Материал')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    created_at = models.DateTimeField(auto_now_add=True)
    favorite = models.BooleanField(default=True, verbose_name='Избранные')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.name.lower().replace(' ', '-')
        self.price = self.old_price * (100 - self.sale) / 100
        num = [self.size[:2], self.size[3:]]
        res = list(range(int(num[0]), int(num[1]), 2))
        self.stock = len(res) + 1
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    color = ColorField(default=True, verbose_name='Цвет')

class Favorite(models.Model):
    products = models.ForeignKey(Product, related_name='favorites', on_delete=models.CASCADE)