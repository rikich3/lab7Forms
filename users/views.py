from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def index(request):
  return render(request, 'sistema/index.html')

def addStudent(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.submit()
      return redirect('list_cursos')
  else:
    form = StudentForm()
  return render, 'sistema/create_curso.html',{'form':form}

# lo uso pa guiarme xd