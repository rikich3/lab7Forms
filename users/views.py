from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def addStudent(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.submit()
      return render(request, 'success.html', {})
  else:
    form = StudentForm()
  return render(request, 'form.html',{'form':form})

# lo uso pa guiarme xd
