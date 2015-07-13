from django.test import TestCase
from django.template import Template, Context, loader

from wagtail.wagtailcore.models import Page


class TestPages(TestCase):

    def test_homepage_return_correct_page(self):
        homepage = Page.objects.get(url_path='/')
        pages = Page.objects.page(homepage)

        # Should only select the homepage
        self.assertEqual(pages.count(), 1)
        self.assertEqual(pages.first(), homepage)





