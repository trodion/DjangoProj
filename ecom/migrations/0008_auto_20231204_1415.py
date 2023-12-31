# Generated by Django 3.0.5 on 2023-12-04 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default='/images/pop-music.jpg', null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 4, 14, 15, 41, 448261), verbose_name='Дата написания'),
        ),
    ]
