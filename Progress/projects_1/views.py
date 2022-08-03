from django.shortcuts import render
from django.http import HttpResponse

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
    page='projects'
    number=10
    context = {'page':page, 'number':number, 'projects': projectList}
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i

    return render(request ,'projects/single-project.html',{'project': projectObj})  



