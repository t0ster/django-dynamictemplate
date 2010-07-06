from django.template.loaders.filesystem import load_template_source \
        as default_template_loader
from middleware import get_current_template


def load_template_source(template_name, template_dirs=None, \
                         template_loader=default_template_loader):    

    template_name = "%s/%s" % (get_current_template(), template_name)

    return template_loader(template_name, template_dirs=template_dirs)
load_template_source.is_usable = True
