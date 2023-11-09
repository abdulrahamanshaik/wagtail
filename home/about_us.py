from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel
from wagtail.images.models import Image
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey

class AboutUsSection(Orderable):
    page = ParentalKey('home.HomePage', related_name='about_us_section')
    about_us_image = models.ImageField(
        upload_to='about_us_images',
        null= True,
        blank=True,
    )

    about_title = models.CharField(max_length=255)
    description = models.TextField()
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('about_us_image'),  
        FieldPanel('about_title'),                 
        FieldPanel('description'),            
        FieldPanel('instagram_link'),          
        FieldPanel('twitter_link'),           
        FieldPanel('facebook_link'),         
    ]

    def __str__(self):
        return self.about_title



 