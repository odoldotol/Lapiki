# Generated by Django 3.2.8 on 2021-11-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_user', '0008_alter_accountsasset_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetsaction',
            name='amount_buy',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='assetsaction',
            name='amount_sell',
            field=models.FloatField(default=0),
        ),
    ]
