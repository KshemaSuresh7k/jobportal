from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import jobseeker,employee
from .forms import AddForm,AddForm1
from django.contrib.auth import authenticate,login as log,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def jobseekerreg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        qualification=request.POST.get('qualification')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        applyfor=request.POST.get('applyfor')
        workingmode=request.POST.get('workingmode')
        username=request.POST.get('username')
        password=request.POST.get('password')
        jobseeker(name=name,address=address,age=age,qualification=qualification,email=email,phonenumber=phonenumber,applyfor=applyfor,workingmode=workingmode,username=username,password=password).save()
    return render(request,'jobseekerreg.html')


def view1(request):
    cr=jobseeker.objects.all()
    return render(request,"view1.html",{'cr':cr})


def detailsview1(request,pk):
    cr=jobseeker.objects.get(id=pk)
    return render(request,"detailsview1.html",{'cr':cr})


def delete(request,pk):
    cr=jobseeker.objects.get(id=pk)
    cr.delete()
    return redirect("view1.html")


def update(request,pk):
    cr=jobseeker.objects.get(id=pk)
    form=AddForm(instance=cr)
    if request.method=="POST":
        form=AddForm(request.POST,instance=cr)
        if form.is_valid:
            form.save()
        return redirect("update")
    return render(request,"login.html",{'form':form})

def about(request):
    return render(request,'about.html')


def employerreg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        age=request.POST.get('age')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        username=request.POST.get('username')
        password=request.POST.get('password')
        employee(name=name,address=address,age=age,email=email,phonenumber=phonenumber,username=username,password=password).save()
    return render(request,'employerreg.html')
    return redirect('home.html')




def view2(request):
    cr=employee.objects.all()
    return render(request,"view2.html",{'cr':cr})


def detailsview2(request,pk):
    cr=employee.objects.get(id=pk)
    return render(request,"detailsview2.html",{'cr':cr})


def delete2(request,pk):
    cr=employee.objects.get(id=pk)
    cr.delete()
    return redirect("view2.html")


def update2(request,pk):
    cr=employee.objects.get(id=pk)
    form=AddForm1(instance=cr)
    if request.method=="POST":
        form=AddForm1(request.POST,instance=cr)
        if form.is_valid:
            form.save()
        return redirect("update2.html")
    return render(request,"update2.html",{'form':form})
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            log(request,user)
            return redirect('loguser')
        else:
            return render(request,'log.html')
    else:
        return render(request,'login.html')

def loguser(request):
    return render(request,'loguser.html')












