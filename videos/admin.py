from django.contrib import admin

# Register your models here.
from .models import Person, ProgramTheme, Program, Course, CourseMaterial, CourseAnnouncement, Category, CourseCategory

admin.site.register(Person)
admin.site.register(ProgramTheme)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(CourseMaterial)
admin.site.register(CourseAnnouncement)
admin.site.register(Category)
admin.site.register(CourseCategory)
