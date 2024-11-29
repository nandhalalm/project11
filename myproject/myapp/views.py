from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Details 
from django.contrib.auth.models import auth
from .models import Marks


def index(request):
    return render(request, 'index1.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        phone = request.POST['phone']
        address = request.POST['address']
        
        if password == confirmpassword:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            user.save()

           
            details = Details.objects.create(
                user=user,
                name=name,
                age=age,
                phone=phone,
                address=address
            )
            details.save()
            return redirect(index)
        else:
            context = {'c': 'Passwords do not match'}
            return render(request, 'forregister.html', context)
    return render(request, 'forregister.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect('home')  
        else:
            context = {
                'message': "Invalid credentials, please try again."  
            }
            return render(request, 'login.html', context)

    return render(request, 'login.html')  

def home(request):
    details = Details.objects.get(user=request.user) 
    return render(request, 'home.html', {'details': details})  

def Logout(request):
    auth.logout(request)  
    context = {
        'message': "Successfully logged out" 
    }
    return render(request, 'login.html', context)  

def profile(request):
    details = Details.objects.get(user=request.user) 
    return render(request, 'profile.html', {'details': details})  

def edit(request):
    details = Details.objects.get(user=request.user)  

    if request.method == 'POST':
        details.name = request.POST['name']
        details.age = request.POST['age']
        details.phone = request.POST['phone']
        details.address = request.POST['address']

        details.save() 
        return redirect(profile) 
    
    else:

        return render(request, 'edit.html', {'details': details})
    

def addmarks(request):
    student = Details.objects.get(user=request.user)
    data = Marks.objects.filter(details=student)

    if request.method == 'POST':
        science = request.POST['science']
        maths = request.POST['maths']
        english = request.POST['english']

        markview=Marks.objects.create(
       
            details=student,
            science=science,
            maths=maths,
            english=english
        )

        markview.save()
        return render(request, 'mark.html', {'data': data})
    else:
        return render(request, 'subject.html')

def viewmark(request):
    student = Details.objects.get(user=request.user)
    data = Marks.objects.filter(details=student)
    return render(request, 'mark.html', {'data': data})


def viewedit(request):
    student = Details.objects.get(user=request.user)  
    marks = Marks.objects.filter(details=student).first()  

    if request.method == 'POST':
        
        marks.science = request.POST['science']
        marks.maths = request.POST['maths']
        marks.english = request.POST['english']
        marks.save() 
        

        return redirect('home') 
    else:
        return render(request, 'editmarks.html', {'marks': marks})


def viewdelete(request, id):
    mark = Marks.objects.get(Marks, id=id)
    mark.delete()
    
    return redirect('home')
   




    
    
