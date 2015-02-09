# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20150209_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='created',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
