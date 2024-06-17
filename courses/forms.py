from django import forms
from .models import Course, NotasAlumnoPorCurso
class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ['name', 'code', 'description', 'image', 'syllabus', 'instructor', 'price', 'duration', 'category', 'level', 'status']
    form_fields = {
      'Codigo': forms.CharField(label='Código', max_length=100, required=False),
    }

class NotasAlumnoPorCursoForm(forms.ModelForm):
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
          'grade': 'Nota'
        }

    def clean_grade(self):
      grade = self.cleaned_data.get('grade')
      if grade < 0 or grade > 20:
          raise forms.ValidationError('La nota debe estar entre 0 y 20')
      return grade