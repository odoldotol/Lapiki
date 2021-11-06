# Generated by Django 3.2.8 on 2021-11-05 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_portfolio', '0003_dataportfoliostockthing_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataportfolio',
            name='cash',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='dataportfolio',
            name='crypto',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='dataportfolio',
            name='saving',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='dataportfolio',
            name='stockthing',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='DataPortfolioSaving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('last_access', models.DateTimeField(auto_now=True)),
                ('symbol', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField(default=0)),
                ('dataportfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_portfolio.dataportfolio')),
            ],
        ),
        migrations.CreateModel(
            name='DataPortfolioCrypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('last_access', models.DateTimeField(auto_now=True)),
                ('symbol', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.FloatField(default=0)),
                ('dataportfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_portfolio.dataportfolio')),
            ],
        ),
        migrations.CreateModel(
            name='DataPortfolioCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('last_access', models.DateTimeField(auto_now=True)),
                ('symbol', models.CharField(max_length=50)),
                ('amount', models.FloatField(default=0)),
                ('dataportfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_portfolio.dataportfolio')),
            ],
        ),
    ]
