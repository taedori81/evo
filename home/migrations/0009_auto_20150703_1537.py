# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20150703_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='section_2_description_1',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='section_2_description_2',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='section_2_description_3',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='section_2_description_4',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
    ]
