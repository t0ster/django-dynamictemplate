import re

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local
from django.conf import settings
from bloom.device import utils
    

_thread_locals = local()
def get_current_request():
    return getattr(_thread_locals, 'request', None)


def is_mobile(request):
    return bool(utils.get_device(request).has_key('mobileDevice'))


def get_current_template():
    return get_current_request().session['template']


def set_template(request, template):
    request.session['last_ua'] = request.META['HTTP_USER_AGENT']
    request.session['template'] = template


class DynamicTemplateMiddleware(object):
    def process_request(self, request):
        """
        Puts the request object in local thread storage so we can access it in
        the template loader.
        """
        if not request.session.has_key('template') or \
        not request.session.has_key('last_ua') or \
        request.session['last_ua'] != request.META['HTTP_USER_AGENT']:
            set_template(request,
                         is_mobile(request) and 'mobile' or 'standard')
        _thread_locals.request = request
