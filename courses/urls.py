from django.urls import path
from courses.views import home, coursePage, SignupView, LoginView, signout, checkout, verifyPayment,my_courses
from django.conf.urls.static import static
from coursesellingapp.settings import MEDIA_URL, MEDIA_ROOT
from django.conf import settings
urlpatterns = [
    path('', home, name='home'),
    path('course/<str:slug>', coursePage, name='coursepage'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', signout, name='logout'),

    path('my-courses', my_courses, name='my-courses'),
    path('check-out/<str:slug>', checkout, name='check-out'),
    path('verify_payment', verifyPayment, name='verify_payment'),
]
urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)