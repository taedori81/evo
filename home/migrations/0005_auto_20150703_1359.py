# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0004_auto_20150703_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_1_image',
            field=models.ForeignKey(related_name='+', blank=True, null=True, to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_1_subtitle_1',
            field=models.CharField(default='Designers', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_1_subtitle_2',
            field=models.CharField(default='Coders', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_1_subtitle_3',
            field=models.CharField(default='Artists', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_1_title',
            field=models.CharField(default='Best Collaboration', max_length=20),
        ),
    ]
