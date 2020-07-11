from django.shortcuts import render,redirect
from projects.models import project
from django.core.mail import send_mail

# Create your views here.

def index(request):
    myProjects = project.objects.all()
    context ={
        'myProjects': myProjects
    } 
    return render(request,'home/index.html',context)

def showProject(request,pk):
    sproject = project.objects.get(id=pk)
    context ={
        'sproject': sproject,
    } 
    return render(request,'home/post.html',context)

def contactme(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        # mobile = request.POST['mobile']
        message = request.POST['message']

        send_mail(
        'Hey darpan you got a new query from: '+name,
        'the message is '+ message,
        'darpansingh5969@gmail.com' + email,
        ['ddev010107@gmail.com'],
        fail_silently=False,
        )
    return redirect('thankyou')

def thankyou(request):
    return render(request,'home/thankyou.html')
    
        


