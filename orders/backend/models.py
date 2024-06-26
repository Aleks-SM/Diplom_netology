from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


USER_TYPE_CHOICES = (
    ('shop', 'Магазин'),
    ('buyer', 'Покупатель')
)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=40, verbose_name='Компания', blank=True) # параметр blank-True говорит Django о том что поле м.б. пустым
    position = models.CharField(max_length=40, verbose_name='Должность', blank=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(max_length=60, validators=[username_validator], unique=True)
    type = models.CharField(max_length=5, verbose_name='Тип пользователя', default='buyer')
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'
        ordering = ('email',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Shop(models.Model):
    """
    name - название магазина
    url - url  или файл из которого загружаются товары
    status  - статус заказа
    user - пользователь
    """
    name = models.CharField(max_length=50, verbose_name='Название', unique=True)
    url = models.CharField(max_length=200, verbose_name='Ссылка', null=True, blank=True)
    status = models.BooleanField(verbose_name='Статус получения заказ', default=True)
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE,
                                blank=True, null=True)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Список магазинов'
        ordering = ('name',)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    name - название категории
    shops - поле связано с табл. Shop
    """
    name = models.CharField(max_length=30, verbose_name='Название')
    shops = models.ManyToManyField(Shop, verbose_name='Магазины',
                                   related_name='categories', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Список категорий'
        ordering = ('name',)

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    name - наименование тоавра
    category - категория товара, поле связано с табл. Category
    """
    name = models.CharField(max_length=60, verbose_name='Наименование')
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 related_name='products', on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Список товаров'
        ordering = ('name',)

    def __str__(self):
        return self.name

class ProductInfo(models.Model):
    model = models.CharField(max_length=60, verbose_name='Not name', blank=True)
    product = models.ForeignKey(Product, verbose_name='Товар', related_name='product_info',
                                on_delete=models.CASCADE, blank=True)
    shop = models.ForeignKey(Shop, verbose_name='Магазин', related_name='product_info',
                             on_delete=models.CASCADE, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')
    price_rrc = models.PositiveIntegerField(verbose_name='Рекомендуемая цена')

    class Meta:
        verbose_name = 'Информация о товаре'
        verbose_name_plural = 'Информация о товарах'

    def __str__(self):
        return self.model

class Parameter(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')

    class Meta:
        verbose_name = 'Наименование параметра'
        verbose_name_plural = 'Список параметров'
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, verbose_name='Информация о товаре',
                                     related_name='product_parametrs',
                                     on_delete=models.CASCADE, blank=True)
    parameter = models.ForeignKey(Parameter, verbose_name='Параметр',
                                  related_name='product_parameters',
                                  on_delete=models.CASCADE, blank=True)
    value = models.CharField(max_length=40, verbose_name='not name')

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Список паратров'


class Contact(models.Model):
    # type
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             related_name='contacts',
                             on_delete=models.CASCADE, blank=True)
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=80, verbose_name='Улица')
    house = models.CharField(max_length=80, verbose_name='Дом')
    apartment = models.CharField(max_length=4, verbose_name='Квартира')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Контакты пользователя'
        verbose_name_plural = 'Список контактов пользователя'

    def __str__(self):
        return f'{self.city} {self.street} {self.house}'


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             related_name='orders',
                             on_delete=models.CASCADE, blank=True)
    date_order = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    status = models.CharField(max_length=15, verbose_name='Статус заказа')
    contact = models.ForeignKey(Contact, verbose_name='Контакт',
                                on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Список заказов'
        ordering = ['date_order']

    def __str__(self):
        return f'{self.date_order} {self.status}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ',
                              on_delete=models.CASCADE, blank=True)
    product_info = models.ForeignKey(ProductInfo, verbose_name='Информация о товаре',
                                     related_name='items_order',
                                     on_delete=models.CASCADE, blank=True)
    # shop =
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Заказанная позиция'
        verbose_name_plural = 'Список позици'
