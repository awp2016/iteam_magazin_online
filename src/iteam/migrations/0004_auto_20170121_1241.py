# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iteam', '0003_auto_20170121_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
    ]
