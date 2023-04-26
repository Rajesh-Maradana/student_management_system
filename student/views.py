from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import Student
import pandas
import json


def hello(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})


def AddStudent(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        fos = request.POST['study']
        gpa = request.POST['gpa']
        try:
            response = Student(first_name=fname, last_name=lname,
                               email=email, field_study=fos, gpa=gpa)
            response.save()
        except Exception as e:
            raise e
    return redirect(hello)


def RemoveStudent(request, s_id):
    a = Student.objects.filter(student_id=s_id)
    try:
        a.delete()
    except Exception as e:
        raise e

    return redirect(hello)


def EditStudent(request, s_id):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        fos = request.POST['study']
        gpa = request.POST['gpa']
        a = Student.objects.filter(student_id=s_id)
        response = a.update(
            first_name=fname, last_name=lname, email=email, field_study=fos, gpa=gpa)

    return redirect(hello)


def AddFromFile(request):
    if request.method == 'POST':
        resp = request.FILES['file'].read()
        excel_data_df = pandas.read_excel(resp)
        json_str = json.loads(excel_data_df.to_json(orient='records'))
        if json_str:
            for data in json_str:
                try:
                    response = Student(
                        first_name=data['First Name'], last_name=data['Last Name'], email=data['Email'], field_study=data['Field Of Study'], gpa=data['GPA'])
                    response.save()
                except Exception as e:
                    raise e

    return redirect(hello)
