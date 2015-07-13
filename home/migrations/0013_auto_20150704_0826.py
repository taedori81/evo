# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20150703_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('label', models.CharField(help_text='The label of the form field', verbose_name='Label', max_length=255)),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')], verbose_name='Field type', max_length=16)),
                ('required', models.BooleanField(verbose_name='Required', default=True)),
                ('choices', models.CharField(help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', blank=True, verbose_name='Choices', max_length=512)),
                ('default_value', models.CharField(help_text='Default value. Comma separated values supported for checkboxes.', blank=True, verbose_name='Default value', max_length=255)),
                ('help_text', models.CharField(blank=True, verbose_name='Help text', max_length=255)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contactpage',
            name='from_address',
            field=models.CharField(blank=True, verbose_name='From address', max_length=255),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='subject',
            field=models.CharField(blank=True, verbose_name='Subject', max_length=255),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='thank_you_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='to_address',
            field=models.CharField(help_text='Optional - form submissions will be emailed to this address', blank=True, verbose_name='To address', max_length=255),
        ),
        migrations.AddField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='form_fields', to='home.ContactPage'),
        ),
    ]
