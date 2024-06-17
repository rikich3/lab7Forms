from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from users.models import Teacher
from users.models import Student
from courses.models import Course

# NotasAlumnosPorCurso
# -----------------
# id_nota (PK)
# id_alumno (FK a Alumnos)
# id_curso (FK a Cursos)
# nota

class NotasAlumnoPorCurso(models.Model):
  id_nota = models.CharField(max_length=100, unique=True, primary_key=True)
  id_alumno = models.ForeignKey(Student, on_delete=models.CASCADE) 
  id_curso = models.ForeignKey(Course, on_delete=models.CASCADE)
  nota = models.IntegerField(
      validators=[MinValueValidator(0), MaxValueValidator(100)]
  )


  #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  def __str__(self):
    return f"({self.id_alumno}) {self.nota}"
