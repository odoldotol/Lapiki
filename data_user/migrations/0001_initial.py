# Generated by Django 3.2.8 on 2021-11-03 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('last_access', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('attribute', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=0, default=0, max_digits=100)),
            ],
        ),
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
        migrations.CreateModel(
            name='PortfoliosAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('last_access', models.DateTimeField(auto_now=True)),
                ('a', models.BooleanField(default=False, help_text='stocks, etf,,, exchange traded financial instruments')),
                ('b', models.BooleanField(default=False, help_text='crypto')),
                ('c', models.BooleanField(default=False, help_text='cash')),
                ('s', models.BooleanField(default=False, help_text='savings')),
                ('p', models.BooleanField(default=False, help_text='pension, retire, insurance, annuity,,,')),
                ('r', models.BooleanField(default=False, help_text='real estate')),
                ('z', models.BooleanField(default=False, help_text='painting, goods etc')),
                ('title', models.CharField(default='', max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=50)),
                ('remark', models.TextField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portfolios.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='AssetsAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('action_time', models.DateTimeField(auto_now_add=True)),
                ('amount_buy', models.DecimalField(decimal_places=0, default=0, max_digits=100)),
                ('amount_sell', models.DecimalField(decimal_places=0, default=0, max_digits=100)),
                ('rabel', models.CharField(choices=[('DF', 'default'), ('QK', '빠른생성'), ('TD', '거래'), ('IO', '입출'), ('IS', '내부거래'), ('US', '수정'), ('IR', '이자'), ('DD', '배당'), ('RT', '월세'), ('PY', '급여')], default='DF', max_length=2)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data_user.portfoliosaccount')),
                ('asset_buy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='action_buy', to='data_user.accountsasset')),
                ('asset_sell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='action_sell', to='data_user.accountsasset')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portfolios.portfolio')),
            ],
        ),
        migrations.AddField(
            model_name='accountsasset',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data_user.portfoliosaccount'),
        ),
        migrations.AddField(
            model_name='accountsasset',
            name='format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data_user.assetformat'),
        ),
        migrations.AddField(
            model_name='accountsasset',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portfolios.portfolio'),
        ),
    ]
