# Generated by Django 2.0.6 on 2018-06-13 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renta_app', '0003_auto_20180613_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveSmallIntegerField(blank=True, default=1, null=True, verbose_name='Количество, шт.'),
        ),
    ]