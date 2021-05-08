# Generated by Django 3.2 on 2021-04-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('totalPrice', models.FloatField(default=0)),
                ('delivery', models.BooleanField(default=False)),
                ('address', models.CharField(default='None', max_length=300)),
                ('paymentMethod', models.CharField(default='cash', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('category', models.CharField(default='None', max_length=30)),
                ('description', models.TextField()),
                ('code', models.CharField(max_length=10)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('productId', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('surname', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
    ]