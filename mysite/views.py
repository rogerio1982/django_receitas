from django.shortcuts import render
from loja.models import Project
def home(request):
 project = Project.objects.all()
 context = {
 'projects': project
 }
 return render(request, 'index.html', context)
def detail(request,pk):
 project = Project.objects.get(pk=pk)
 context = {
 'project': project
 }
 return render(request, 'detalhes.html', context)