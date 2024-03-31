from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    compamy = models.CharField(max_length=40, verbose_name='Компания', unique=True)
    position = models.CharField(max_length=40, verbose_name='Должность')
    username = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.compamy}'

class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    url = models.CharField(max_length=200, verbose_name='Ссылка', null=True, blank=True)
    status = models.BooleanField(verbose_name='Статус получения заказ', default=True)
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Список магазинов'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    shops = models.ManyToManyField(Shop, verbose_name='Магазины')

    class Meta:
        verbose_name = ('Категория')
        verbose_name_plural = ('Список категорий')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='Наименование')
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 related_name='products', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Список товаров'

    def __str__(self):
        return self.name

class ProductInfo(models.Model):
    model = models.CharField(max_length=60, verbose_name='Not name')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, verbose_name='Магазин', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')
    price_rrc = models.PositiveIntegerField(verbose_name='Рекомендуемая цена')

    class Meta:
        verbose_name = 'Информация о товаре'
        verbose_name_plural = 'Информация о товарах'

    def __str__(self):
        return self.name

class Parameter(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        pass

class ProdustParameter:
    product_info
    parameter
    value

    class Meta:
        pass
class Order:
    user
    dt
    status

    class Meta:
        pass

class OrderItem:
    order
    product
    shop
    quantity

    class Meta:
        pass

class Contact(models.Model):
    type
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='contacts', on_delete=models.CASCADE)
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=80, verbose_name='Улица')
    house = models.CharField(max_length=80, verbose_name='Дом')
    apartment = models.CharField(max_length=4, verbose_name='Квартира')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Контакты пользователя'
        verbose_name_plural = 'Список контактов пользователя'
