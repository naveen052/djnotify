# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_title', models.CharField(max_length=150)),
                ('post_body', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
