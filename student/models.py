from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=90)
    email = models.EmailField(max_length=254, unique=True)
    field_study = models.CharField(max_length=100)
    gpa = models.FloatField()

    def __str__(self) -> str:
        return self.first_name
