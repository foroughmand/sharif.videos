import django; 
django.setup()
from videos.models import *
import sys


first=True
for l in sys.stdin:
	x = l.split(';')
	if first:
		names = x
		first=False
		continue
	
	print 'line: ', x

	part = x[9]
	session = x[8]
	if (part == '-'): part = ''

	course_all = Course.objects.filter(old_id = x[12])
	if len(course_all) == 0:
		print 'course not found = ', x[12]
		continue
	course = course_all[0]

	cm_all = CourseMaterial.objects.filter(course_id=course.id, name=session+'-'+part)
	if (len(cm_all) == 0):
		cm = CourseMaterial(course_id=course.id, name=session+'-'+part)
		cm.save()
	else:
	 	cm = cm_all[0]

	cm.video_url = 'http://213.233.161.92/videos/' + x[0] + '.' + x[13]
	cm.video_name = x[13]
	cm.save()
