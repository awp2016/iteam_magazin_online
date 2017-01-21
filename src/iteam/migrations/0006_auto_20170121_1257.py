# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from iteam.models import User


# def super_user(apps, schema_editor):
    # try:
        # User.objects.get(email="admin@admin.com")
    # except:
        # User.objects.create_superuser(email="admin@admin.com", password="admin")


class Migration(migrations.Migration):

    dependencies = [
        ('iteam', '0005_auto_20170121_1256'),
    ]

    operations = [
            # migrations.RunPython(super_user),
    ]
