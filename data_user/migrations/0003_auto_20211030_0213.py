# Generated by Django 3.2.8 on 2021-10-30 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_user', '0002_auto_20211029_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsasset',
            name='amount',
            field=models.DecimalField(decimal_places=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='assetsaction',
            name='amount_buy',
            field=models.DecimalField(decimal_places=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='assetsaction',
            name='amount_sell',
            field=models.DecimalField(decimal_places=0, max_digits=100),
        ),
    ]