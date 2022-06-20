from django.db import models
from django.forms import ValidationError

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    descrintion = models.TextField(verbose_name='Описание')
    images = models.ImageField(upload_to='news_image', verbose_name='Фотография')

    class Meta:
        ordering = ('title', )
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

class Slider(models.Model):
    urlka = models.URLField(verbose_name='Ссылка', blank=True, null=True)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

    def __str__(self):
        return self.urlka

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_image', verbose_name='Фотография')
    slider = models.ForeignKey(Slider,on_delete=models.CASCADE, related_name='slider' )

class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    decription = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ('title', )
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class AboutUsImage(models.Model):
    adout_us_image = models.ImageField(upload_to='about_us', blank=True, null=True )
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='about_us')

class PublicOffert(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        ordering = ('title', )
        verbose_name = 'Публичная офферта'
        verbose_name_plural = 'Публичная офферта'

    def __str__(self):
        return self.title

# проверка на валидацию картинок
def custom_validator(value):
    valid_formats = ['png', 'svg']
    if not any([True if value.name.endswith(i) else False for i in valid_formats]):
        raise ValidationError(f'{value.name} is not a valid image format')
        
class OurAdvantages(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='advantage_image', verbose_name='Фотография', validators=[custom_validator])

    class Meta:
        ordering = ('title', )
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'

    def __str__(self):
        return self.title

class CallBack(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя',)
    phone_num = models.CharField(max_length=100, verbose_name='Номер')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время обращения')
    callback_type = models.CharField(max_length=100, default='Обратный звонок', verbose_name='Тип обращения')
    status_call = models.BooleanField(default=False, verbose_name='Позвонили?')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'

    def __str__(self):
        return f'{self.name} {self.created_at}'

class HelpImage(models.Model):
    images = models.ImageField(upload_to='helpers_image', verbose_name='Фотография')

class Helpers(models.Model):
    question = models.TextField(verbose_name='Вопросы')
    answer = models.TextField(verbose_name='Ответ')
    image = models.ForeignKey(HelpImage, on_delete=models.CASCADE, related_name='image', verbose_name='Фотография')

    class Meta:
        verbose_name = 'Вопрос и Ответ'
        verbose_name_plural = 'Вопросы и Ответы'

    def __str__(self):
        return self.answer
    
