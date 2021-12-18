from django.db import models
from django.db.models.fields import URLField

class Job(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заказ')
    price = models.CharField(max_length=250, verbose_name='Цена')
    views = models.CharField(max_length=250, verbose_name='Просмотры')
    responses = models.CharField(max_length=250, verbose_name='Отклики')
    time = models.CharField(max_length=250, verbose_name='Время')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

