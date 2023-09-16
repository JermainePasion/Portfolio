from django.shortcuts import render

def home(request):
    return render(request, 'portfol/home.html')

def main(request):
    return render (request,'portfol/main.html')

def about(request):
    return render(request,'portfol/about.html')