from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectList = [
    {
        'id' : '1',
        'title' : "Ecommerce Website",
        'description' :'Fully functional ecommerce website'
    },

     {
        'id' : '2',
        'title' : "Portfolio Website",
        'description' :'This was a project where I built out my prtfolio'
    },

     {
        'id' : '3',
        'title' : "Social Website",
        'description' :'Awesome open soursce project I am still working'
    },
]

def projects(request):

   projects = Project.objects.all
   context = {'projects': projects}
   return render(request,'projects/projects.html', context)

def project(request,pk):
    
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    print('projectObj:', projectObj)
    return render(request ,'projects/single-project.html',{'project': projectObj})  



