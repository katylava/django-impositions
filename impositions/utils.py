from datetime import datetime
from django.utils.importlib import import_module
from django.conf import settings
from .models import Composition, COMPDIR

imaging_module = '.backends.{0}'.format(settings.IMPOSITION_IMAGING_BACKEND)
engine = import_module(imaging_module, package='impositions')



def output_composition(comp_id, fmt='JPEG'):
    comp = Composition.objects.get(pk=comp_id)
    output = engine.ImagingBackend(comp.template.image.path, COMPDIR)

    for region in comp.regions.all():
        if region.region.content_type == 'text':
            output.impose_text(
                region.fill.text,
                region.region.box,
                region.fill.font.font_file.path,
                region.fill.fg_color,
                region.fill.font_size
            )
        elif region.region.content_type == 'image':
            output.impose_image(region.fill.image.path, region.region.box)
        else:
            raise NotImplementedError

    filepath = "{0}/{1}_{2}.jpg".format(
        COMPDIR,
        comp.template.name,
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    )

    output.save(fmt, filepath)
    comp.file_path = filepath
    comp.save()
    return filepath

