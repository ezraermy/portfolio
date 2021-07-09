from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
        return render(request, "projects/index.html", {
            "projects": Project.objects.all()
        })

def detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, "projects/detail.html", {
        "project": project,
    })