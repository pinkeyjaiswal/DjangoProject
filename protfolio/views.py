from django.shortcuts import render,redirect
from Banking.models import Banking,header
from django.shortcuts import redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def Home(request):
    B=Banking.objects.all
    return render(request,'home.html',{'Banking':B})
 
def adds(request, blog_id):
     #header=header.objects.all
     if request.method=="POST":
          if request.POST['title']:
              k=get_object_or_404(Banking, pk=blog_id)
              k=header()
              k.title=request.POST['title']
               #header=get_object_or_404(header, pk=blog_id)
               #name_01=request.POST['title']
               # new_add=header(title=name_o1)
              k.save()
              return redirect('Home')
     else:
          return render(request,'add.html',{'error':"no product found"})
     return render(request,'add.html',{'header':k})





def details(request,blog_id):
    d=get_object_or_404(Banking,pk=blog_id)
    return render(request,'details.html',{'det':d})
def base(request):
    return render(request,'base.html')
def SIGNUP(request):
     if request.method=="POST":
          if request.POST['password']==request.POST['confirm']:
               try:
                    user=User.objects.get(username=request.POST['username'])
                    return render(request,'signup.html',{'error':"user already exit"})
               except:
                    user=User.objects.create_user(request.POST['username'],password=request.POST['password'])
                    auth.login(request,user)
                    return redirect('Home')
          else:
                return render(request,'signup.html',{'error':"password did not match"})
     return render(request,'signup.html')
def Login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('Home')
        else: 
            return render(request,'login.html',{'error':"user password is incorrect"})
    else:
        return render(request,'login.html')
@login_required(login_url='/signup')
def create(request):
     if request.method=="POST":
          if request.FILES['image'] and request.POST['summary']:
               j=Banking()
               j.image=request.FILES['image']
               j.summary=request.POST['summary']
               j.save()
               return redirect('Home')
     else:
          return render(request,'create.html',{'error':"no product found"})
     return render(request,'create.html')
def logout(request):
     if request.method=='POST':
          auth.logout(request)
          return redirect('Home')
def HTML(request):
     return render(request,'HTML.html')


