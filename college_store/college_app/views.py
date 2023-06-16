from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def home(request):
    return render(request, "index.html")
def form(request):
    return render(request, "form.html")
def detail(request):
    return render(request,'detail.html')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('detail')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,'login.html')




def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username alredy taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
                return redirect('login')


        else:

            messages.info(request,"password does not match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')



