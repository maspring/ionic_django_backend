# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsframework', '0002_auto_20150604_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to=b'media/pictures/'),
        ),
    ]
