# Generated by Django 3.2.8 on 2021-11-04 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_user', '0003_auto_20211103_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountsasset',
            name='classi',
            field=models.CharField(default='', max_length=50),
        ),
    ]
