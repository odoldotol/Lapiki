# Generated by Django 3.2.8 on 2021-11-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('amount_decimal_places', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialAccountsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30)),
                ('a', models.BooleanField(default=False, help_text='stocks, etf,,, exchange traded financial instruments')),
                ('b', models.BooleanField(default=False, help_text='crypto')),
                ('c', models.BooleanField(default=False, help_text='cash')),
                ('s', models.BooleanField(default=False, help_text='savings')),
                ('p', models.BooleanField(default=False, help_text='pension, retire, insurance, annuity,,,')),
            ],
        ),
    ]
