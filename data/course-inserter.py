import django; django.setup()
from videos.models import *
import sys


first=True
for l in sys.stdin:
	x = l.split(';')
	if first:
		names = x
		first=False
		continue
	p_all = Program.objects.filter(old_id=x[2]+'-'+x[4])

	if (len(p_all) == 0):
		p = Program(old_id = x[2] + '-' + x[4], program_theme_id=2, title=x[2] + '-' + x[4])
		p.save()
	else:
	 	p = p_all[0]

	ins = Person.objects.get(short_id=x[6])

	c_all = Course.objects.filter(old_id = x[0])
	if (len(c_all) == 0):
		c = Course(old_id=x[0], title=x[3], instructor_id=ins.id, program_id=p.id, image_url='http://videos.math.sharif.ir/images/thumbs/' + x[0] + '.jpg', bg_image_url='http://videos.math.sharif.ir/images/courses/bgs/'+x[0]+'.jpg')
		c.save()
	else:
		c = c_all[0]

	if x[8] != '':
		for cc in x[8].split(','):
			cat_all = Category.objects.filter(old_id=cc)
			if (len(cat_all) == 0):
				cat = Category();
				cat.save()
			else:
				cat = cat_all[0]
			ccx = CourseCategory(course_id=c.id, category_id=cat.id)
			ccx.save()
