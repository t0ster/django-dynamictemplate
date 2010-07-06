from django.conf.urls.defaults import * #@UnusedWildImport

from views import change_template


urlpatterns = patterns("",
    (r"^change-template/", change_template),
)
