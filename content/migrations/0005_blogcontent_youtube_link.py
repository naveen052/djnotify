# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20150209_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcontent',
            name='youtube_link',
            field=models.URLField(default=datetime.datetime(2015, 2, 9, 6, 5, 57, 390123, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
