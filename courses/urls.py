from django.urls import path
from courses.views import home, coursePage
from django.conf.urls.static import static
from coursesellingapp.settings import MEDIA_URL, MEDIA_ROOT
from django.conf import settings
urlpatterns = [
    path('', home, name='home'),
    path('course/<str:slug>', coursePage, name='coursepage')
]
urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)