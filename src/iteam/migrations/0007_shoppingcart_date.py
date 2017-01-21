# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('iteam', '0006_auto_20170121_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
