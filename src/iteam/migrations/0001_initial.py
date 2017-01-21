# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('email', models.EmailField(unique=True, db_index=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
                ('avatar', models.ImageField(upload_to='user')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('productName', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imageSource1', models.ImageField(blank=True, null=True, upload_to='')),
                ('imageSource2', models.ImageField(blank=True, null=True, upload_to='')),
                ('imageSource3', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to='iteam.User', serialize=False, related_name='cart')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(to='iteam.Product'),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='products',
            field=models.ManyToManyField(through='iteam.Order', to='iteam.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(to='iteam.ShoppingCart'),
        ),
    ]
