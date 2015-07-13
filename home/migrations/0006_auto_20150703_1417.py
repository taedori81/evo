# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0005_auto_20150703_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_2_image',
            field=models.ForeignKey(null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_subtitle_1',
            field=models.CharField(default='Skillful', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_subtitle_2',
            field=models.CharField(default='Professional', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_subtitle_3',
            field=models.CharField(default='Artistic', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_title',
            field=models.CharField(default='Craftsmanship', max_length=20),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_3_image',
            field=models.ForeignKey(null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_3_subtitle_1',
            field=models.CharField(default='Unique', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_3_subtitle_2',
            field=models.CharField(default='Personal', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_3_subtitle_3',
            field=models.CharField(default='Stand Out', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_3_title',
            field=models.CharField(default='Creativity', max_length=20),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_4_image',
            field=models.ForeignKey(null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_4_subtitle_1',
            field=models.CharField(default='Responsible', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_4_subtitle_2',
            field=models.CharField(default='Reliable', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_4_subtitle_3',
            field=models.CharField(default='Persistent', max_length=10),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_4_title',
            field=models.CharField(default='Accountability', max_length=20),
        ),
    ]
