# Generated by Django 3.2.8 on 2021-11-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_user', '0007_alter_accountsasset_classi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsasset',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
