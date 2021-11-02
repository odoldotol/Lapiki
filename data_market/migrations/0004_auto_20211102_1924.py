# Generated by Django 3.2.8 on 2021-11-02 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_market', '0003_auto_20211031_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickersymbol',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tickersymbol',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tickersymbol',
            name='previousClose',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tickersymbol',
            name='regularMarketPreviousClose',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
