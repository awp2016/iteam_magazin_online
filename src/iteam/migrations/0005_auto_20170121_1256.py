# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iteam', '0004_auto_20170121_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('products', models.ManyToManyField(to='iteam.Product', through='iteam.Order')),
                ('user', models.ForeignKey(to='iteam.User', related_name='cart')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(to='iteam.ShoppingCart', default=0),
            preserve_default=False,
        ),
    ]
