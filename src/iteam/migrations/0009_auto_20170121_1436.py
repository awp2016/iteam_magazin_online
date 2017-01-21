# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('iteam', '0008_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='date',
            field=models.DateField(blank=True, default=None),
        ),
    ]
