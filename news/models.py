from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify 
from django.db.models.signals import pre_save

from django.template.defaultfilters import slugify

import string 
from django.utils.text import slugify 
import random 

# Create your models here.
class News(models.Model):
    title = models.CharField(_('title'), max_length=250)
    description = models.TextField(_('description'))
    image = models.ImageField(_('url'), upload_to="media/news/%Y/%m/%d/", null=True, blank=True)
    date = models.DateField(_('date'), auto_now_add=True)
    slug = models.SlugField(_('slug'), max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"slug": self.slug})

def unique_slug_generator(instance):
    constant_slug = slugify(instance.title)
    slug = constant_slug
    num = 0
    Klass = instance.__class__
    while Klass.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=constant_slug, num=num)
    return slug

def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug or instance.title != News.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever, sender=News)