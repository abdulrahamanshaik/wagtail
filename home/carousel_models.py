from django.db import models
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.images.models import Image
from wagtail.admin.panels import FieldPanel
from wagtail.models import  Orderable

class CarouselItem(Orderable):
    page = ParentalKey('home.HomePage', related_name='carousel_items')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='+')
    caption = RichTextField(blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

    def __str__(self):
        return self.caption

