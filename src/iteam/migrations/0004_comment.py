# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('iteam', '0003_auto_20170121_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(to='iteam.Product')),
            ],
        ),
    ]
