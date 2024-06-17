from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Teacher
from users.models import Student

# NotasAlumnosPorCurso
# -----------------
# id_nota (PK)
# id_alumno (FK a Alumnos)
# id_curso (FK a Cursos)
# nota


class NotasAlumnoPorCurso(models.Model):
  id_nota = models.CharField(max_length=100, unique=True, primary_key=True)
  id_alumno = models.CharField(max_length=255, blank=False, null=False)
  id_curso = models.TextField(blank=True, null=False)
  nota = models.IntegerField(
      validators=[MinValueValidator(0), MaxValueValidator(100)]
  )


  #teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  def __str__(self):
    return f"({self.id_alumno}) {self.nota}"
