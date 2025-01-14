# Generated by Django 3.2.8 on 2021-10-11 01:11

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import polls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('memberID', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'участник',
                'verbose_name_plural': 'участники',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.IntegerField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
                ('price', models.IntegerField()),
                ('imageSource', models.ImageField(default='img/image.png', upload_to=polls.models.custom_save_path, verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('typeID', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('typeName', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'тип',
                'verbose_name_plural': 'типы',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactionID', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('approvalStatus', models.CharField(max_length=10)),
                ('transactionDate', models.DateField(auto_now_add=True)),
                ('memberID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.member')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product')),
            ],
            options={
                'verbose_name': 'транзакция',
                'verbose_name_plural': 'транзакции',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('raitingID', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.SmallIntegerField()),
                ('memberID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.member')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product')),
            ],
            options={
                'verbose_name': 'оценка',
                'verbose_name_plural': 'оценки',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.producttype'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentID', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('commentDate', models.DateField()),
                ('memberID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.member')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cartID', models.IntegerField(primary_key=True, serialize=False)),
                ('productIDs', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('productQuantities', django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), size=None)),
                ('quantity', models.IntegerField()),
                ('memberID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.member')),
            ],
            options={
                'verbose_name': 'корзина',
                'verbose_name_plural': 'корзины',
            },
        ),
    ]
