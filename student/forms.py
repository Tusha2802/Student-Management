from django import forms
from student.models import Student,Login,Course

class StuForm(forms.ModelForm):
     class Meta:
          model=Student
          fields="__all__";

class LoginForm(forms.ModelForm):
     class Meta:
          model=Login;
          fields="__all__";

class CourseForm(forms.ModelForm):
     class Meta:
          model=Course;
          fields="__all__";
          
