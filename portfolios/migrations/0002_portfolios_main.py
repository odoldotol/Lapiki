# Generated by Django 3.2.8 on 2021-10-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolios',
            name='main',
            field=models.BooleanField(default=False, verbose_name='main portfolio?'),
        ),
    ]
