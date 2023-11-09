from django.db import models
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.images.models import Image
from wagtail.admin.panels import FieldPanel
from wagtail.models import  Orderable,Page

class ContactUs(Orderable):
    page = ParentalKey('home.HomePage', related_name='contact_us')
    contact_banner = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='+')
    contact_number = models.CharField(max_length=20)
    gmail = models.EmailField()
    address = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('contact_banner'),
        FieldPanel('contact_number'),
        FieldPanel('gmail'),
        FieldPanel('address'),
    ]

    def __str__(self):
        return self.title