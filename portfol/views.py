from django.shortcuts import render, redirect
from .models import Contact

def home(request):
    return render(request, 'portfol/home.html')

def main(request):
    return render (request,'portfol/main.html')

def about(request):
    return render(request,'portfol/about.html')

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
    return render(request,'portfol/contact.html')

