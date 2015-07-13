# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0013_auto_20150704_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='contactpage',
            name='contact_description',
            field=models.CharField(max_length=100, blank=True, default='Contact us if you have any question, recommendations or just for saying hello.'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='contact_header',
            field=models.CharField(max_length=20, default='Contact us'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='contact_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', null=True, blank=True),
        ),
    ]
