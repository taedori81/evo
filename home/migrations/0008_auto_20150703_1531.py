# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0007_auto_20150703_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicespage',
            name='section_1_image',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_1_sub_heading',
            field=models.CharField(max_length=500, default='We create digital experiences for brands and companies by using creativity and technology.'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_description_1',
            field=wagtail.wagtailcore.fields.RichTextField(default='What is Branding? It is the marketing practice of creating a name, symbol or design that identifies and differentiates a product from other products. If you plan to start up your own business, you need to Brand your company first.'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_description_2',
            field=wagtail.wagtailcore.fields.RichTextField(default='Even if your website is built with good tech, good functionality, You will have no pay attention if your web site has a bad user experience,  user interface.   We offer modern, simple, mobile ready, responsive design and a good user experience for your web site.'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_description_3',
            field=wagtail.wagtailcore.fields.RichTextField(default='It is all about the code, code code! We like coding. We build website with well-known, well-established, well-supported programming language and framework, so the website is very easily editable, customizable and expandable.'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_description_4',
            field=wagtail.wagtailcore.fields.RichTextField(default="OK. You've got the best, unique, competitive service or product. How do you let the world know that you exist? Posting your web address in facebook, twitter or instagram? Well. That is not enough. You need to expose yourself to the world in better way than that."),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_heading',
            field=models.CharField(max_length=500, default='Wide range of design and development services provided with a personal experience.'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_image',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_sub_heading_1',
            field=models.CharField(max_length=20, default='Branding'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_sub_heading_2',
            field=models.CharField(max_length=20, default='Web Design'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_sub_heading_3',
            field=models.CharField(max_length=20, default='Web Programming'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='section_2_sub_heading_4',
            field=models.CharField(max_length=20, default='Marketing'),
        ),
    ]
