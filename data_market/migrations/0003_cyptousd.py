# Generated by Django 3.2.8 on 2021-11-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_market', '0002_exchangerate'),
    ]

    operations = [
        migrations.CreateModel(
            name='CyptoUSD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
