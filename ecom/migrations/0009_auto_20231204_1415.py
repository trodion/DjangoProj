# Generated by Django 3.0.5 on 2023-12-04 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_auto_20231204_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 4, 14, 15, 53, 104539), verbose_name='Дата написания'),
        ),
    ]