from django.contrib import admin
from courses.models import Course, Tag, Learning, Prerequisite, Video, Payment, UserCourse

# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.TabularInline):
    model = Video

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin,LearningAdmin,PrerequisiteAdmin, VideoAdmin]
    list_display = ['name','get_price','get_discount','active']

    def get_discount(self, course):
        return f'{course.discount}%'

    def get_price(self, course):
        return f'₹{course.price}'

    get_discount.short_description = "DISCOUNT"
    get_price.short_description = "PRICE"

admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment)
admin.site.register(UserCourse)