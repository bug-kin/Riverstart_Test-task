from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='наименование',
        max_length=64,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(
        verbose_name='наименование',
        max_length=80,
        unique=True,
        blank=False,
        null=False,
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        default=0
    )
    quantity = models.IntegerField(
        verbose_name='количество',
        default=1,
    )
    description = models.TextField(
        verbose_name='описание',
    )
    is_deleted = models.BooleanField(
        verbose_name='удалено',
    )
    created = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='изменения',
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
