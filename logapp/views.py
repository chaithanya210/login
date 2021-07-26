from django.shortcuts import render
from .models import signup_table
def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")
def login(request):
    return render(request,"login.html")
# Create your views here.
def signup_save(request):
    if request.method=="POST":
        a=signup_table()
        a.name=request.POST.get("name")
        a.username=request.POST.get("uname")
        a.password=request.POST.get("pswd")
        a.confirmpassword=request.POST.get("cpswd")
        a.save()
        return render(request,"login.html")

def login_save(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pswd")

        if(signup_table.objects.filter(username=username,password=password).exists()):
            user=signup_table.objects.get(username=username,password=password)
            request.session['user_name']=user.username
            return render(request,"main.html")
        else:

            return render(request,"login.html",{'msg':'Invalid username or password'})



