from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

app_name = 'videos'

urlpatterns = [
#url(r'^$', views.index, name='index'),
#url(r'^(?P<course_id>[0-9]+)/$', views.course, name='course'),
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^index$', views.IndexView.as_view(), name='index2'),
	url(r'^course/(?P<pk>[0-9]+)/$', views.CourseView.as_view(), name='course'),
	url(r'^search/$', views.search, name='search'),
#url(r'^search/(?P<program_id>[0-9]+)/(?P<instructor_id>[0-9]+)/(?P<category_id>[0-9]+)/$', views.search, name='search'),
	url(r'^about$', TemplateView.as_view(template_name='videos/about.html'), name='about'),
	url(r'^terms$', TemplateView.as_view(template_name='videos/terms.html'), name='terms'),
	url(r'^contact$', TemplateView.as_view(template_name='videos/contact.html'), name='contact'),
]
