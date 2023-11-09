from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,InlinePanel
from .carousel_models import CarouselItem
from .about_us import AboutUsSection
from .latest_stories import LatestStories
from .contact_us import ContactUs



class HomePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel('carousel_items', label="Carousel Items"),
        InlinePanel('about_us_section', label="About Us Section"),
        InlinePanel('latest_stories', label="Latest Stories"),
        InlinePanel('contact_us', label="Contact Us"),
        
    ]

    class Meta:
        verbose_name = "Home Page"

