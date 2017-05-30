from django.conf.urls import url
from . import views

# For template tagging we need to set this global name, it must match what is in the {%  %} for the href
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]
