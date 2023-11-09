from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,InlinePanel,MultiFieldPanel
from modelcluster.fields import ParentalKey

class AboutUsPage(Page):
    about_title = models.CharField(max_length=255)
    about_description = models.TextField()
    content_panels = Page.content_panels + [
        FieldPanel('about_title'),
        FieldPanel('about_description'),
        MultiFieldPanel(
            [
                InlinePanel('main_head_of_company', label="Main Head of the Company"),
                InlinePanel('team_members', label="Team Members"),
            ],
            heading="About Us Sections"
        ),
    ]

class MainHeadOfCompany(models.Model):
    page = ParentalKey(AboutUsPage, related_name='main_head_of_company')
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Select an image for the main head of the company.'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()

    panels = [
        FieldPanel('main_image'),
        FieldPanel('title'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    page = ParentalKey(AboutUsPage, related_name='team_members')
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Select an image for the team member.'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()

    panels = [
        FieldPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.title

