# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import content.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20150209_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcontent',
            name='picture',
            field=models.ImageField(max_length=255, null=True, upload_to=content.models.content_file_location, blank=True),
            preserve_default=True,
        ),
    ]
