from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from portfolio.models import Project,Contact

# Create your views here.
def home(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request,'home.html',context)
 

def project(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request,'project.html',context)


def project_d(request, id):
    project = get_object_or_404(Project,id=id)
    context={
        'project': project
        }
    return render(request,'project_d.html',context)

def contact(request):
    p=Project.objects.all()
    if request.method ==  "POST":
        n=request.POST['name']
        e=request.POST['email']
        m=request.POST['message']
        
        Contact.objects.create(name=n,email=e,message=m)
    context={
            'p':p
        }
    return render(request,'contact.html',context)



def about(request):
    return render(request,'about.html') 

def skills(request):
    return render(request,'skills.html') 