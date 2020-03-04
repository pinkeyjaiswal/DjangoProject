from django.shortcuts import render

# Create your views here.
def Banking(request):
    return render(request,'home.html')
def header(request, blog_id):
    return render(request,'home.html')