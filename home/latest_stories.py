from django.db import models
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.images.models import Image
from wagtail.admin.panels import FieldPanel
from wagtail.models import  Orderable

class LatestStories(Orderable):
    page = ParentalKey('home.HomePage', related_name='latest_stories')
    stories_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='+')
    stories_caption = RichTextField(blank=True)
    stories_description = models.TextField()

    panels = [
        FieldPanel('stories_image'),
        FieldPanel('stories_caption'),
        FieldPanel('stories_description'),
    ]

    def __str__(self):
        return self.stories_caption

