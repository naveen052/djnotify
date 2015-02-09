# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_blogcontent_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='created',
            field=models.DateField(default=datetime.datetime(2015, 2, 9, 3, 9, 16, 346065, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
