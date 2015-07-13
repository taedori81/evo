from __future__ import unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from .forms import ContactForm


class HomePage(Page):

    section_1_title = models.CharField(max_length=20, blank=False, default="Best Collaboration")
    section_1_subtitle_1 = models.CharField(max_length=20, blank=False, default="Designers")
    section_1_subtitle_2 = models.CharField(max_length=20, blank=False, default="Coders")
    section_1_subtitle_3 = models.CharField(max_length=20, blank=False, default="Artists")
    section_1_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_2_title = models.CharField(max_length=20, blank=False, default="Craftsmanship")
    section_2_subtitle_1 = models.CharField(max_length=20, blank=False, default="Skillful")
    section_2_subtitle_2 = models.CharField(max_length=20, blank=False, default="Professional")
    section_2_subtitle_3 = models.CharField(max_length=20, blank=False, default="Artistic")
    section_2_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_3_title = models.CharField(max_length=20, blank=False, default="Creativity")
    section_3_subtitle_1 = models.CharField(max_length=20, blank=False, default="Unique")
    section_3_subtitle_2 = models.CharField(max_length=20, blank=False, default="Personal")
    section_3_subtitle_3 = models.CharField(max_length=20, blank=False, default="Stand Out")
    section_3_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_4_title = models.CharField(max_length=20, blank=False, default="Accountability")
    section_4_subtitle_1 = models.CharField(max_length=20, blank=False, default="Responsible")
    section_4_subtitle_2 = models.CharField(max_length=20, blank=False, default="Reliable")
    section_4_subtitle_3 = models.CharField(max_length=20, blank=False, default="Persistent")
    section_4_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = [
        FieldPanel('title', classname="full title"),

        FieldPanel('section_1_title', classname="full"),
        FieldPanel('section_1_subtitle_1', classname="full"),
        FieldPanel('section_1_subtitle_2', classname="full"),
        FieldPanel('section_1_subtitle_3', classname="full"),
        ImageChooserPanel('section_1_image'),

        FieldPanel('section_2_title', classname="full"),
        FieldPanel('section_2_subtitle_1', classname="full"),
        FieldPanel('section_2_subtitle_2', classname="full"),
        FieldPanel('section_2_subtitle_3', classname="full"),
        ImageChooserPanel('section_2_image'),

        FieldPanel('section_3_title', classname="full"),
        FieldPanel('section_3_subtitle_1', classname="full"),
        FieldPanel('section_3_subtitle_2', classname="full"),
        FieldPanel('section_3_subtitle_3', classname="full"),
        ImageChooserPanel('section_3_image'),

        FieldPanel('section_4_title', classname="full"),
        FieldPanel('section_4_subtitle_1', classname="full"),
        FieldPanel('section_4_subtitle_2', classname="full"),
        FieldPanel('section_4_subtitle_3', classname="full"),
        ImageChooserPanel('section_4_image'),

    ]


class ServicesPage(Page):

    @property
    def get_contact_page(self):
        return ContactPage.objects.live()

    section_1_sub_heading = models.CharField(max_length=500, blank=False,
                                   default="We create digital experiences for brands and companies by using creativity and technology.")
    section_1_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    section_2_heading = models.CharField(max_length=500, blank=False,
                                         default="Wide range of design and development services provided with a personal experience.")
    section_2_sub_heading_1 = models.CharField(max_length=20, blank=False, default="Branding")
    section_2_description_1 = models.TextField()
    section_2_sub_heading_2 = models.CharField(max_length=20, blank=False, default="Web Design")
    section_2_description_2 = models.TextField()
    section_2_sub_heading_3 = models.CharField(max_length=20, blank=False, default="Web Programming")
    section_2_description_3 = models.TextField()
    section_2_sub_heading_4 = models.CharField(max_length=20, blank=False, default="Marketing")
    section_2_description_4 = models.TextField()
    section_2_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('section_1_sub_heading', classname="full title"),
        ImageChooserPanel('section_1_image'),

        FieldPanel('section_2_heading', classname="full"),

        FieldPanel('section_2_sub_heading_1', classname="full"),
        FieldPanel('section_2_description_1', classname="full"),

        FieldPanel('section_2_sub_heading_2', classname="full"),
        FieldPanel('section_2_description_2', classname="full"),

        FieldPanel('section_2_sub_heading_3', classname="full"),
        FieldPanel('section_2_description_3', classname="full"),

        FieldPanel('section_2_sub_heading_4', classname="full"),
        FieldPanel('section_2_description_4', classname="full"),

        ImageChooserPanel('section_2_image'),
    ]


class SpecialOfferPage(Page):
    main_header_1 = models.CharField(max_length=20, blank=False, default="Special")
    main_header_2 = models.CharField(max_length=20, blank=False, default="Offer")
    main_sub_header = models.CharField(max_length=50, blank=False, default="Limited Time Offer")

    main_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('main_header_1', classname="full"),
        FieldPanel('main_header_2', classname="full"),
        FieldPanel('main_sub_header', classname="full"),

        ImageChooserPanel('main_image'),
    ]


class TeamPage(Page):
    taehwan_avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    josh_avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    kimmy_avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    sean_avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = [
        ImageChooserPanel('taehwan_avatar'),
        ImageChooserPanel('josh_avatar'),
        ImageChooserPanel('kimmy_avatar'),
        ImageChooserPanel('sean_avatar'),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='form_fields')


class ContactPage(AbstractEmailForm):
    thank_you_text = RichTextField(blank=True)
    contact_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    contact_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    contact_header = models.CharField(max_length=20, blank=False, default="Contact us")
    contact_description = models.CharField(max_length=100, blank=True, default="Contact us if you have any question, recommendations or just for saying hello.")


ContactPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('contact_header', classname="full"),
    FieldPanel('contact_description', classname="full"),
    ImageChooserPanel('contact_image'),
    ImageChooserPanel('contact_icon'),

    FieldPanel('thank_you_text', classname="full"),
    InlinePanel('form_fields', label="Form fields"),
    MultiFieldPanel([
        FieldPanel('to_address', classname="full"),
        FieldPanel('from_address', classname="full"),
        FieldPanel('subject', classname="full"),
    ], "Email")
]




















