# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0011_auto_20150703_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampage',
            name='josh_avatar',
            field=models.ForeignKey(blank=True, related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='teampage',
            name='kimmy_avatar',
            field=models.ForeignKey(blank=True, related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='teampage',
            name='sean_avatar',
            field=models.ForeignKey(blank=True, related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='teampage',
            name='taehwan_avatar',
            field=models.ForeignKey(blank=True, related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
    ]
