from django import forms
from .models import Student, User

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['id', 'name', 'email',]
    
  def clean(self):
    cleaned_data = super().clean()
    student_id = cleaned_data.get('id')
    # Check if there's already a Student with the same student_id
    if Student.objects.filter(id=student_id).exists():
        raise forms.ValidationError('Ya existe un estudiante con ese id')
    return cleaned_data
  
  def submit(self, commit=True):
    instance = super().save(commit=False)
    if commit:
      instance.save()
    return instance