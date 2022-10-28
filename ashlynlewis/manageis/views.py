from django.shortcuts import render
from django.db.models.query_utils import PathInfo
from django.shortcuts import render
from .models import StudentEmployee,StudentWork,Supervisor,AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions,DjangoAdminLog,DjangoContentType,DjangoMigrations,DjangoSession
from django.db import connection


# Create your views here.
def indexPageView(request) :
    return render(request, 'manageis/index.html')


def firetablePageView(request) :
    student = StudentEmployee.objects.all()
    supervisor = Supervisor.objects.all()

    #attempting to join the tables (attempt failed)
    cursor = connection.cursor()
    query = "SELECT emp_first, emp_last, international,is_male,email,phone FROM Student_Employee JOIN Student_Work ON Student_Employee.byu_id =  Student_Work.byu_id"
    cursor.execute(query)
    results=cursor.fetchall()

    context = {
        "student":student,
        "supervisor":supervisor,
        "results": results,
    }
    return render(request, 'manageis/firetable.html',context) 


def editSingleStudent(request, byu_id):
    data = StudentEmployee.objects.get(byu_id = byu_id)
    context = {
        "record":data
    }
    return render(request, "manageis/editStudent.html", context)

def updateSingleStudent(request):
    if request.method == 'POST':
        byu_id = request.POST['byu_id']
        student = StudentEmployee.objects.get(byu_id=byu_id)
        student.emp_first = request.POST['emp_first']
        student.emp_last = request.POST['emp_last']
        student.international = request.POST.get('international') == 'on'
        student.is_male = request.POST.get('is_male') == 'on'
        print("student.international: ", student.international)
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.save()

    return firetablePageView(request)

# needs work
# yes it does
def deleteEmployeePageView(request, byu_id) :
    data = StudentEmployee.objects.get(byu_id = byu_id)
    data.delete()
    return firetablePageView(request)
