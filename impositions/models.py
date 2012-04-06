import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

REGION_TYPES = (
    ('text', 'Text'),
    ('image', 'Image'),
)

if not hasattr(settings, 'COMPDIR'):
    COMPDIR = os.path.join(settings.MEDIA_ROOT, 'impositions', 'comps')
else:
    COMPDIR = settings.COMPDIR
COMPSTORAGE = FileSystemStorage(location=COMPDIR)

class TemplateFont(models.Model):
    name = models.CharField(max_length=100)
    font_file = models.FileField(upload_to='impositions/fonts')

    def __unicode__(self):
        return self.name

class TemplateImageFill(models.Model):
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='impositions/assets', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    font = models.ForeignKey(TemplateFont, null=True, blank=True)
    font_size = models.IntegerField(null=True, blank=True)
    bg_color = models.CharField(max_length=50, null=True, blank=True)
    fg_color = models.CharField(max_length=50, null=True, blank=True)
    border_color = models.CharField(max_length=50, null=True, blank=True)
    border_size = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.description or self.text or self.image.url

class TemplateImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='impositions/templates')

    def __unicode__(self):
        return self.name

class TemplateImageRegion(models.Model):
    template = models.ForeignKey(TemplateImage, related_name='regions')
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    content_type = models.CharField(max_length=16, choices=REGION_TYPES)
    top_left = models.CommaSeparatedIntegerField(max_length=12)
    bottom_right = models.CommaSeparatedIntegerField(max_length=12)
    allowed_fonts = models.ManyToManyField(TemplateFont, null=True, blank=True)
    allowed_colors = models.TextField(null=True, blank=True)
    allowed_sizes = models.CommaSeparatedIntegerField(max_length=50, null=True, blank=True)
    allowed_images = models.ManyToManyField(TemplateImageFill, null=True, blank=True)
    # TODO: add alignment property to properly position fills that are smaller than the region

    @property
    def size(self):
        t, l, b, r = self.box
        return (r - l, b - t)

    @property
    def box(self):
        return eval(self.top_left) + eval(self.bottom_right)

    def __unicode__(self):
        return "{0} (Template: {1})".format(
            self.name,
            self.template.__unicode__()
        )


class Composition(models.Model):
    template = models.ForeignKey(TemplateImage)
    description = models.CharField(max_length=200)
    file_path = models.FilePathField(path=COMPDIR, recursive=True, blank=True)
    # TODO: add format property so user can choose format (jpg, png, pdf)

    def __unicode__(self):
        return "[{0}] {1}".format(
            self.template.__unicode__(),
            self.description
        )

class CompositionRegion(models.Model):
    comp = models.ForeignKey(Composition, related_name='regions')
    region = models.ForeignKey(TemplateImageRegion)
    fill = models.ForeignKey(TemplateImageFill)

    def __unicode__(self):
        return "{0}::{1}".format(
            self.comp.__unicode__(),
            self.region.name
        )
