# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_blogcontent_youtube_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogcontent',
            name='post_body',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogcontent',
            name='youtube_link',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
