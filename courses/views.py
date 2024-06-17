from django.shortcuts import render, redirect
from .forms import CourseForm, NotasAlumnoPorCursoForm
from .models import Course, NotasAlumnoPorCurso
from users.models import Student

def index(request):
  return render(request, 'sistema/index.html')

def create_curso(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      form.submit()
      return redirect('list_cursos')
  else:
    form = CourseForm()
  return render, 'sistema/create_curso.html',{'form':form}

def list_cursos(request):
  cursos = Course.objects.all()
  return render(request, 'sistema/list_cursos.html', {
    'cursos':cursos
  })

def addGrade(request):
  if request.method == 'POST':
    form = NotasAlumnoPorCursoForm(request.POST)
    if form.is_valid():
      form.submit()
      return redirect('success')
  else:
    form = NotasAlumnoPorCursoForm()
  return render(request, 'sistema/add_grade.html', {'form': form})