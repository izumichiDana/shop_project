from django.db import models
from django.forms import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    descrintion = models.TextField(verbose_name='Описание')
    images = models.ImageField(upload_to='news_image', verbose_name='Фотография')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

class Slider(models.Model):
    urlka = models.URLField(verbose_name='Ссылка', blank=True)

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

    def __str__(self):
        return f'{self.urlka} {self.image}'

class SliderImage(models.Model):
    slider_image = models.ImageField(upload_to='slider_image',  blank=True, null=True, verbose_name='Фотография',)
    slider = models.ForeignKey(Slider,on_delete=models.CASCADE, related_name='slider',)

class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    decription = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class AboutUsImage(models.Model):
    adout_us_image = models.ImageField(upload_to='about_us', blank=True, null=True )
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='about_us')

class PublicOffert(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
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
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'

    def __str__(self):
        return self.title

class CallBack(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя',)
    phone_num = PhoneNumberField(blank=True, verbose_name='Номер')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время обращения')
    callback_type = models.CharField(max_length=100, default='Обратный звонок', verbose_name='Тип обращения')
    status_call = models.BooleanField(default=False, verbose_name='Позвонили?')

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'

    def __str__(self):
        return f'{self.name} {self.created_at}'

class HelpImage(models.Model):
    images = models.ImageField(upload_to='helpers_image', blank=True, null=True, verbose_name='Фотография')

    class Meta:
        verbose_name = ' Вопрос и Ответ'
        verbose_name_plural = 'Вопросы и Ответы'

    def __str__(self):
        return f'{self.images}'

class Helpers(models.Model):
    question = models.TextField(verbose_name='Вопросы')
    answer = models.TextField(verbose_name='Ответы')
    help = models.ForeignKey(HelpImage, on_delete=models.CASCADE, related_name='image', blank=True, null=True, verbose_name='Фотография')


class Futer(models.Model):
    futer_image = models.ImageField(upload_to='futer_image', verbose_name='Фото для Футера',)
    heder_image = models.ImageField(upload_to='heder_image', verbose_name='Фото для Хедера',)
    information = models.TextField(verbose_name='Текстовая Информация')
    phone_number = PhoneNumberField(blank=True, verbose_name='Номер')

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'

    def __str__(self):
        return f'{self.information} {self.phone_number}'

CONTACT_LINKS = (
    ('Number', 'Number'),
    ('Mail', 'Mail'),
    ('Telegram', 'Telegram'),
    ('WhatsApp', 'WhatsApp'),
    ('Instagram', 'Instagram'),
)

class FuterLink(models.Model):
    name = MultiSelectField(choices=CONTACT_LINKS, max_length=254, max_choices=3, db_index=True, default=('NUMBER', 'Number'), verbose_name='Выбор из списка')
    number = models.CharField(max_length=30, blank=True, verbose_name='введенные данные')
    num = PhoneNumberField(blank=True, verbose_name='Номер')
    whatsapp = models.CharField(max_length=100, blank=True, verbose_name='Whatsapp')
    instagram = models.CharField(max_length=100, blank=True, verbose_name='Instagram')
    mail = models.CharField(max_length=100, blank=True, verbose_name='Почта')
    telegram = models.CharField(max_length=100, blank=True,  verbose_name='Telegram')

    class Meta:
        verbose_name = 'Ссылка футера'
        verbose_name_plural = 'Ссылки футера'

    def __str__(self):
        return f'{self.num} {self.whatsapp} {self.instagram} {self.mail} {self.telegram} {self.name} {self.number}'

    def save(self, *args, **kwargs): 
        print(self.name)
        if 'WhatsApp' in self.name: 
            self.whatsapp = f'http://wa.me/{self.number}/' 
        if 'Telegram' in self.name: 
            self.telegram = f'https://t.me/{self.number}/' 
        if 'Instagram' in self.name: 
            self.instagram = f'https://www.instagram.com/{self.number}/' 
        if 'Mail' in self.name: 
            self.mail = f'https://mail.doodle.com/{self.number}/' 
        if 'Number' in self.name: 
            self.num=f'+996{self.number}'

        super(FuterLink, self).save(*args, **kwargs)



    


    
