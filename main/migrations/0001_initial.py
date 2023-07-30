# Generated by Django 4.2.1 on 2023-07-16 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lusher_results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(blank=True, null=True, verbose_name='Результат')),
                ('date_of_result', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Дата отзыва')),
            ],
            options={
                'verbose_name': 'Люшер',
                'verbose_name_plural': 'Результаты Люшера',
            },
        ),
    ]