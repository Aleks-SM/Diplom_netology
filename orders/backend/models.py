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
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Список товаров'

    def __str__(self):
        return self.name

class ProductInfo(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, verbose_name='Магазин', on_delete=models.CASCADE)
    name = models.CharField(max_length=60, verbose_name='Not name')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')
    price_rrc = models.PositiveIntegerField(verbose_name='Рекомендуемая цена')

    class Meta:
        verbose_name = 'Информация о товаре'
        verbose_name_plural = 'Информация о товарах'