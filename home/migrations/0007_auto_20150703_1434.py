# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150703_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='section_1_subtitle_1',
            field=models.CharField(max_length=20, default='Designers'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_1_subtitle_2',
            field=models.CharField(max_length=20, default='Coders'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_1_subtitle_3',
            field=models.CharField(max_length=20, default='Artists'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_2_subtitle_1',
            field=models.CharField(max_length=20, default='Skillful'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_2_subtitle_2',
            field=models.CharField(max_length=20, default='Professional'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_2_subtitle_3',
            field=models.CharField(max_length=20, default='Artistic'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_3_subtitle_1',
            field=models.CharField(max_length=20, default='Unique'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_3_subtitle_2',
            field=models.CharField(max_length=20, default='Personal'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_3_subtitle_3',
            field=models.CharField(max_length=20, default='Stand Out'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_4_subtitle_1',
            field=models.CharField(max_length=20, default='Responsible'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_4_subtitle_2',
            field=models.CharField(max_length=20, default='Reliable'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_4_subtitle_3',
            field=models.CharField(max_length=20, default='Persistent'),
        ),
    ]
