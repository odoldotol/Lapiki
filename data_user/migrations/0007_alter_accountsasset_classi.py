# Generated by Django 3.2.8 on 2021-11-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_user', '0006_accountsasset_classi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsasset',
            name='classi',
            field=models.CharField(max_length=50),
        ),
    ]