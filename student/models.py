from django.db import models

# Create your models here.
class Student(models.Model):
     Name=models.CharField(max_length=20);
     Email=models.EmailField();
     Password=models.CharField(max_length=20);
     Contact=models.CharField(max_length=20);
     Qualification=models.CharField(max_length=20);
     
     class Meta:
          db_table="Student";

class Login(models.Model):
     UserName=models.EmailField();
     Password=models.CharField(max_length=20)
     class Meta:
          db_table="Login";

class Course(models.Model):
     #course_choices=(('1','1'),('2','2'),('3','3'),('4','4'))
     c1=models.CharField(max_length=10)
     c2=models.CharField(max_length=10)
     c3=models.CharField(max_length=10)
     c4=models.CharField(max_length=10)
     class Meta:
          db_table="Course";
