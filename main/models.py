from django.db import models
from datetime import datetime

def default_datetime(self): return datetime.now()


class Lusher_results(models.Model):
    result = models.TextField('Результат', null=True, blank=True)
    date_of_result = models.DateField('Дата отзыва', null=True, blank=True, default=datetime.now)

    def __str__(self):
         
        return f"{self.result} {self.date_of_result}"
    
    # def to_json(self):
    #         return {
    #             'author_of_fdback': self.author_of_fdback,
    #         }
    
    class Meta:
        verbose_name = 'Люшер'
        verbose_name_plural = 'Результаты Люшера'


class LusherColorPair(models.Model):
    color_pair = models.CharField('Пара цветов', max_length=100)
    interpretation = models.TextField('Интерпретация')

    class Meta:
        verbose_name = 'Пара цветов'
        verbose_name_plural = 'Пары цветов'