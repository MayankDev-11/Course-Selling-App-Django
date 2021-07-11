import math
from django.shortcuts import render, redirect, HttpResponse
from courses.models import Course, Payment, UserCourse
import razorpay
from coursesellingapp.settings import *
from time import time
from django.views.decorators.csrf import csrf_exempt
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    if action == 'create_payment':
        try:
            user_course = UserCourse.objects.get(user=user,course=course)
            error = "You are aldready enrolled in this Course"
        except:
            pass

        if error is  None:
            amount = int((course.price - (course.price * course.discount * 0.01))*100)
            currency = "INR"
            notes = {
                'email':user.email,
                'name':f'{user.first_name} {user.last_name}',
            }
            receipt = f'coursesellingapp_{int(time())}'
            order = client.order.create({'receipt' : receipt, 'notes' : notes, 'amount' : amount, 'currency' : currency})
            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()

    context = {
        'course':course,
        'order':order,
        'payment':payment,
        'user':user,
        'error':error
    }
    return render(request,'courses/check_out.html', context=context)

@csrf_exempt
def verifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        context={}
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            payment = Payment.objects.get(order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True

            userCourse = UserCourse(user=payment.user, course=payment.course)
            userCourse.save()

            payment.user_course = userCourse
            payment.save()

            return redirect('my-courses')
        except:
            return HttpResponse("Invalid Payment Details")