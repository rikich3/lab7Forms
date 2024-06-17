from django import forms
from .models import Course, NotasAlumnoPorCurso
from django.forms import ValidationError
#Para guardar
class GenericForm(forms.ModelForm):
    def submit(self, commit=True):
      instance = super().save(commit=False)
      if commit:
         instance.save()
      return instance

class CourseForm(GenericForm):
  class Meta:
      model = Course
      fields = ['name', 'code', 'description']
      
  code = forms.CharField(label="Código", max_length=50)
  name = forms.CharField(label="Nombre",max_length=50)
  description = forms.CharField(widget=forms.Textarea, label="Descripcion")

class NotasAlumnoPorCursoForm(GenericForm):
#   NotasAlumnosPorCurso
# -----------------
# id_nota (PK)
# id_alumno (FK a Alumnos)
# id_curso (FK a Cursos)
# nota
    class Meta:
        model = NotasAlumnoPorCurso
        fields = ['student', 'course', 'grade']
        
        labels = {
            'student': 'Alumno',
            'course': 'Curso',
            'grade': 'Mota'
        }

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if grade < 0 or grade > 20:
            raise ValidationError('La nota debe estar entre 0 y 20')
        return grade