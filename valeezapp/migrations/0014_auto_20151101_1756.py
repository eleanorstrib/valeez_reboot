# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('valeezapp', '0013_remove_voyage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='valeez',
            name='voyage',
            field=models.OneToOneField(null=True, to='valeezapp.Voyage'),
        ),
        migrations.AddField(
            model_name='voyage',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
