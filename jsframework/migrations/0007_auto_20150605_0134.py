# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0006_auto_20150605_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/content/pictures'), upload_to=b''),
        ),
    ]
