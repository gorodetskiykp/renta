from django.db import models


class Category(models.Model):
    category = models.CharField('Категория', max_length=50, blank=True, null=True)
    price_per_month = models.PositiveSmallIntegerField('Цена за месяц, руб.', blank=True, null=True, default=0)
    price_per_day = models.PositiveSmallIntegerField('Цена за день, руб.', blank=True, null=True, default=0)
    price_per_hour = models.PositiveSmallIntegerField('Цена за час, руб.', blank=True, null=True, default=0)
    img = models.CharField('Ссылка на изображение', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(models.Model):
    city = models.ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField('Описание', max_length=500, blank=True, null=True)
    price_per_month = models.PositiveSmallIntegerField('Цена за месяц, руб.', blank=True, null=True)
    price_per_day = models.PositiveSmallIntegerField('Цена за день, руб.', blank=True, null=True)
    price_per_hour = models.PositiveSmallIntegerField('Цена за час, руб.', blank=True, null=True)
    img = models.CharField('Ссылка на изображение', max_length=500, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField('Количество, шт.', blank=True, null=True, default=1)
    description = models.TextField('Описание', blank=True, null=True, default='')

    def __str__(self):
        return '{} {}'.format(self.category, self.name)

    def save(self, *args, **kwargs):
        if not self.price_per_month:
            self.price_per_month = self.category.price_per_month
        if not self.price_per_day:
            self.price_per_day = self.category.price_per_day
        if not self.price_per_hour:
            self.price_per_hour = self.category.price_per_hour
        if not self.img:
            self.img = self.category.img
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class City(models.Model):
    city = models.CharField('Город', max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return '{}'.format(self.city)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'