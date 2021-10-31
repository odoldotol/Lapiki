# Generated by Django 3.2.8 on 2021-10-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TickerSymbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=50, unique=True)),
                ('symbol', models.CharField(max_length=50, unique=True)),
                ('shortName', models.CharField(max_length=50)),
                ('longName', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=50)),
                ('financialCurrency', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('market', models.CharField(max_length=50)),
                ('exchange', models.CharField(max_length=50)),
                ('marketCap', models.CharField(max_length=50)),
                ('trailingPE', models.CharField(max_length=50)),
                ('dividendYield', models.CharField(max_length=50)),
                ('trailingEps', models.CharField(max_length=50)),
                ('beta', models.CharField(max_length=50)),
                ('currentPrice', models.CharField(max_length=50)),
            ],
        ),
    ]
