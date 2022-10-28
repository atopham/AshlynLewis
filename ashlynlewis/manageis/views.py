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


# needs work
def deleteEmployeePageView(request, byu_id) :
    data = StudentEmployee.objects.get(byu_id = byu_id)
    data.delete()
    return firetablePageView(request)
