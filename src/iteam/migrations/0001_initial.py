# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('email', models.EmailField(unique=True, max_length=255, db_index=True)),
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
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('author', models.ForeignKey(to='iteam.User')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('source', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('productName', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('products', models.ManyToManyField(through='iteam.Order', to='iteam.Product')),
                ('user', models.ForeignKey(to='iteam.User', related_name='cart')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(to='iteam.ShoppingCart'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(to='iteam.Product'),
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(to='iteam.Product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(to='iteam.Product'),
        ),
    ]
