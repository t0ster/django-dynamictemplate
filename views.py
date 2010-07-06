from django.views.generic.simple import redirect_to
from middleware import set_template


def change_template(request):
    template = request.GET.get('template', 'standard')
    set_template(request, template)
    url = request.META.get("HTTP_REFERER", "/")
    return redirect_to(request, url=url)