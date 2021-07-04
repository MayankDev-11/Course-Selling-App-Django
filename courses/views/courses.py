from django.shortcuts import render
from courses.models import Course, Video


def coursePage(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number =1
    video = Video.objects.get(serial_number=serial_number, course=course)
    context = {
        'course':course,
        'video':video,
        'videos':videos,
    }
    return render(request,'courses/course_page.html', context=context)
