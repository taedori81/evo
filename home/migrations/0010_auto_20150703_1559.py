# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150703_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='section_2_description_1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='section_2_description_2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='section_2_description_3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='section_2_description_4',
            field=models.TextField(),
        ),
    ]
