# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0010_auto_20150703_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialofferpage',
            name='main_header_1',
            field=models.CharField(default='Special', max_length=20),
        ),
        migrations.AddField(
            model_name='specialofferpage',
            name='main_header_2',
            field=models.CharField(default='Offer', max_length=20),
        ),
        migrations.AddField(
            model_name='specialofferpage',
            name='main_image',
            field=models.ForeignKey(to='wagtailimages.Image', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+'),
        ),
        migrations.AddField(
            model_name='specialofferpage',
            name='main_sub_header',
            field=models.CharField(default='Limited Time Offer', max_length=50),
        ),
    ]
