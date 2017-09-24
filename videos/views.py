from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from random import randint

from .models import *

class IndexView(generic.ListView):
	template_name = 'videos/index.html'
	context_object_name = 'data'


	def get_queryset(self):
		"""Return current semester coureses."""
		randomindex = 1
		searchbg_name = 'some courses'
		searchbg_link = "http://front.math.sharif.ir/92";
		return {'current_course_list': Course.objects.filter(program__is_current=True),
			'randomindex': randomindex,
			'searchbg_name': searchbg_name,
			'searchbg_link': searchbg_link,
			'instructors': Person.objects.all(),
			'programs': Program.objects.all(),
			'categories': CourseCategory.objects.all(),
			}

def search(request):
	o = Course.objects
	if ('category_id' in request.POST and request.POST['category_id'] != ""):
		o = o.filter(category__id=request.POST['category_id'])
	if ('instructor_id' in request.POST and request.POST['instructor_id'] != ""):
		o = o.filter(instructor__id=request.POST['instructor_id'])
	if ('program_id' in request.POST and request.POST['program_id'] != ""):
		o = o.filter(program__id=request.POST['program_id'])
	return render(request, 'videos/search.html', {
			'courses': o.all(),
		})

class CourseView(generic.DetailView):
	model = Course
	template_name = 'videos/course.html'

# Create your views here.
#def index(request):
#	current_course_list = Course.objects.filter(program__is_current=True)
#	#output = ', '.join([c.title + ' ' + c.program.title for c in current_course_list])
#	#return HttpResponse(template.render(context, request))
#	#template = loader.get_template('videos/index.html')
#	context = {
#		'current_course_list': current_course_list,
#	}
#
#	return render(request, 'videos/index.html', context)
#
#def course(request, course_id):
#	try:
#		course = Course.objects.get(pk=course_id)
#	except Course.DoesNotExist:
#		raise Http404("Course does not exist")
#	return render(request, 'videos/course.html', {'course': course})
##return HttpResponse("You're looking at question course %s." % course_id)
####################################################################################


