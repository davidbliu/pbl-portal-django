# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_google_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.CharField(default='no_name', max_length=100),
            preserve_default=False,
        ),
    ]
