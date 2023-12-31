from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


class GenericPage(Page):
    banner_title = models.CharField(max_length=100,default="Welcome to my Genericpage")

    introduction = models.TextField(blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    author = models.ForeignKey(
        "Author",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"

    )
    

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("introduction"),
        FieldPanel("banner_image"),
        FieldPanel("author"),
    ]

    @register_snippet
    class Author(models.Model):
        name = models.CharField(max_length=100)
        title = models.CharField(max_length=100,blank=True)
        company_name = models.CharField(max_length=100,blank=True)
        company_url = models.URLField(blank=True)
        image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name="+"
        )

        #Not required to create explicitly wagtail will create explicitly"

        panels = [
            FieldPanel("name"),
            FieldPanel("title"),
            FieldPanel("company_name"),
            FieldPanel("company_url"),
            FieldPanel("image")
        ]

        def __str__(self):
            return self.name
