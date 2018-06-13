from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ayomi_auth.urls')),
    url(r'^$', RedirectView.as_view(url='/login/')),
]
