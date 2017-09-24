import django; django.setup()
from videos.models import *
import sys


for l in sys.stdin:
	x = l.split('\t')
	p = Person(name=x[2], family=x[3], initials=x[4], family_en=x[0], photo_url=x[1], short_id=x[0])
	p.save()
