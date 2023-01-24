from django.shortcuts import render,redirect
from .models import *

from django.contrib import messages


# Create your views here.
def home(request):
    views = {}
    views['feedbacks'] = Feedback.objects.all()
    views['services'] = Services.objects.all()
    views['portpolio_cats'] = Portfoliocategory.objects.all()
    views['portpolios'] = Portfolio.objects.all()

    return render(request,'index.html',views)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            messege = message
        )
        data.save()
        messages = {}
        messages['message']= 'The form is submitted!'
        return render(request, 'contact.html',messages)

    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def price(request):
    return render(request, 'price.html')


def services(request):
    return render(request, 'services.html')

def blog_home(request):
    views = {}
    views['blogs'] = Blog.objects.all()
    views['blog_cat'] = BlogCategory.objects.all()

    return render(request,'blog-home.html',views)

def blog_single(request):
    return render(request,'blog-single.html')