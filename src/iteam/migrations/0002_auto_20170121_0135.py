# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iteam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imageSource1',
            new_name='imagesource1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='imageSource2',
            new_name='imagesource2',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='imageSource3',
            new_name='imagesource3',
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(default='M', max_length=1, choices=[('M', 'Male'), ('F', 'Female')]),
        ),
    ]
