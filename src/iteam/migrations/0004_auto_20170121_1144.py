# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iteam', '0003_auto_20170121_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('source', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='imagesource1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='imagesource2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='imagesource3',
        ),
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(to='iteam.Product'),
        ),
    ]
