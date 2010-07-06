import os
from django import template
from django.conf import settings
from ..middleware import get_current_template

register = template.Library()
TEMPLATES = None

@register.inclusion_tag('show_templates.html')
def show_templates():
    global TEMPLATES
    if not TEMPLATES:
        templates_path = os.path.join(settings.PROJECT_ROOT, 'templates')
        TEMPLATES = filter(lambda x: os.path.isdir(
                                        os.path.join(templates_path, x)),
                           os.listdir(templates_path))
    return {'templates': TEMPLATES,
            'current': get_current_template()}
