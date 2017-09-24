from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=200)
	family = models.CharField(max_length=200)
	initials = models.CharField(max_length=100)
	name_en = models.CharField(max_length=200)
	family_en = models.CharField(max_length=200)
	photo_url = models.CharField(max_length=200)
	home_page_url = models.CharField(max_length=200,null=True)
	position = models.CharField(max_length=200,null=True)
	short_id = models.CharField(max_length=100)

	def __unicode__(self):
		return u''+self.name + ' ' + self.family

#Semester, Frontiers, Shafahi, ...
class ProgramTheme(models.Model):
	title = models.CharField(max_length=200)
	def __unicode__(self):
		return u''+self.title

#
class Category(models.Model):
	title = models.CharField(max_length=200)
	old_id = models.IntegerField(null=True)
	def __unicode__(self):
		return u''+self.title

#Each Semester is a program
class Program(models.Model):
	title = models.CharField(max_length=200)
	program_theme = models.ForeignKey(ProgramTheme, on_delete=models.CASCADE)
	is_current = models.BooleanField(default=False)
	start_date = models.DateTimeField('program start date', null=True)
	finish_date = models.DateTimeField('program finish date', null=True)
	old_id = models.CharField(max_length=100)
	def __unicode__(self):
		return u''+self.title

class Course(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	instructor = models.ForeignKey(Person, on_delete=models.CASCADE)
	image_url = models.CharField(max_length=200)
	bg_image_url = models.CharField(max_length=200)
	old_id = models.CharField(max_length=200)
	#category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	#announcements
	#materials
	def __unicode__(self):
		return u''+self.title + ' ' + self.program.title

class CourseCategory(models.Model):
	course = models.ForeignKey(Course)
	category = models.ForeignKey(Category)

	def __unicode(self):
		return self.course + ' ' + self.category

#class CourseSession(models.Model):
#	name = models.CharField(max_length=200)
#	description = models.CharField(max_length=200)
#	order = models.IntegerField(default=0)
#	#this_session_instructors


class CourseMaterial(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200, null=True)
	order = models.IntegerField(default=0, null=True)
	video_url = models.CharField(max_length=200, null=True)
	video_name = models.CharField(max_length=200, null=True)
	handout_url = models.CharField(max_length=200, null=True)
	handout_name = models.CharField(max_length=200, null=True)
	def __unicode__(self):
		return u''+self.name + ' ' + self.course.title + ' ' + self.course.program.title

class CourseAnnouncement(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=200)
	def __unicode__(self):
		return u''+self.title + ' ' + self.course.title

