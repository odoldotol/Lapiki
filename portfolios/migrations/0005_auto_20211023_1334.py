# Generated by Django 3.2.8 on 2021-10-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0004_alter_portfolios_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolios',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Mainportfolio',
        ),
    ]