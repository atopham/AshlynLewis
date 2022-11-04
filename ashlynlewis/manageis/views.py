from django.shortcuts import render
from django.db.models.query_utils import PathInfo
from django.shortcuts import render
from .models import StudentEmployee,StudentWork,Supervisor,AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions,DjangoAdminLog,DjangoContentType,DjangoMigrations,DjangoSession
from django.db import connection
from .filters import StudentFilter, SupervisorFilter, WorkFilter
from django.http import HttpResponse
import csv

# Create your views here.

def indexPageView(request) :
    return render(request, 'manageis/index.html')


def firetablePageView(request) :
    student = StudentEmployee.objects.all()
    supervisor = Supervisor.objects.all()
    work = StudentWork.objects.all()

    myStudentFilter = StudentFilter(request.GET, queryset=student)
    student = myStudentFilter.qs

    mySupervisorFilter = SupervisorFilter(request.GET, queryset=supervisor)
    supervisor = mySupervisorFilter.qs


    cursor = connection.cursor()
    query = "SELECT se.byu_id,se.emp_first, se.emp_last, se.international,se.is_male,se.email,se.phone,sw.exptected_hours, sw.semester, sw.year, sw.class_code, sw.emp_record, sw.supervisor_id, sw.hire_date, sw.pay_rate,sw.last_pay_increase_date, sw.pay_increase_amount, sw.increase_input_date, sw.program_year, sw.is_pay_grad_tuition, sw.name_change_completed,sw.notes, sw.terminated, sw.termination_date, sw.survey_sent, sw.eform_submitted, sw.eform_submission_date, sw.auth_work_received, sw.auth_work_email_sent, sw.byu_name FROM Student_Employee se JOIN Student_Work sw ON se.byu_id =  sw.byu_id"
    cursor.execute(query)
    results=cursor.fetchall()

    context = {
        "work": work,
        "student":student,
        "supervisor":supervisor,
        "results": results,
        "myStudentFilter": myStudentFilter,
        "mySupervisorFilter": mySupervisorFilter,        
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
    data = StudentWork.objects.get(byu_id = byu_id)
    data.delete()
    data = StudentEmployee.objects.get(byu_id = byu_id)
    data.delete()
    return firetablePageView(request)



###############---The following are for exporting CSV files---########################

def sup_export_to_csv(request):
    supervisors = Supervisor.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=supervisor_export.csv'
    writer = csv.writer(response)
    writer.writerow(['supervisor id', 'First Name', 'Last Name'])
    supervisor_fields = supervisors.values_list('supervisor_id', 'supervisor_first', 'supervisor_last')
    for supervisor in supervisor_fields:
        writer.writerow(supervisor)
    return response

def stud_export_to_csv(request):
    students = StudentEmployee.objects.all()
    works = StudentWork.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=student_export.csv'
    writer = csv.writer(response)
    writer.writerow([
        'BYU ID', 'first name', 'last name', 'international', 'is male?', 'email', 'phone',
        'BYU ID', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name'
    ])
    student_fields = students.values_list('byu_id', 'emp_first', 'emp_last', 'international', 'is_male', 'email', 'phone')
    work_fields = works.values_list('byu_id', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name')
    for student in student_fields:
        for work in work_fields:
            if student[0] == work[0]:
                writer.writerow(student+work)
    return response


def summer_export_to_csv(request):
    students = StudentEmployee.objects.all()
    works = StudentWork.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=summer_export.csv'
    writer = csv.writer(response)
    writer.writerow([
        'BYU ID', 'first name', 'last name', 'international', 'is male?', 'email', 'phone',
        'BYU ID', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name'
    ])
    student_fields = students.values_list('byu_id', 'emp_first', 'emp_last', 'international', 'is_male', 'email', 'phone')
    work_fields = works.values_list('byu_id', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name')
    for student in student_fields:
        for work in work_fields:
            if (student[0] == work[0]) and (work[2] == 'Summer') :
                writer.writerow(student+work)
    return response

def fall_export_to_csv(request):
    students = StudentEmployee.objects.all()
    works = StudentWork.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=fall_export.csv'
    writer = csv.writer(response)
    writer.writerow([
        'BYU ID', 'first name', 'last name', 'international', 'is male?', 'email', 'phone',
        'BYU ID', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name'
    ])
    student_fields = students.values_list('byu_id', 'emp_first', 'emp_last', 'international', 'is_male', 'email', 'phone')
    work_fields = works.values_list('byu_id', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name')
    for student in student_fields:
        for work in work_fields:
            if (student[0] == work[0]) and (work[2] == 'Fall') :
                writer.writerow(student+work)
    return response

def winter_export_to_csv(request):
    students = StudentEmployee.objects.all()
    works = StudentWork.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=winter_export.csv'
    writer = csv.writer(response)
    writer.writerow([
        'BYU ID', 'first name', 'last name', 'international', 'is male?', 'email', 'phone',
        'BYU ID', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name'
    ])
    student_fields = students.values_list('byu_id', 'emp_first', 'emp_last', 'international', 'is_male', 'email', 'phone')
    work_fields = works.values_list('byu_id', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name')
    for student in student_fields:
        for work in work_fields:
            if (student[0] == work[0]) and (work[2] == 'Winter') :
                writer.writerow(student+work)
    return response

def spring_export_to_csv(request):
    students = StudentEmployee.objects.all()
    works = StudentWork.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=spring_export.csv'
    writer = csv.writer(response)
    writer.writerow([
        'BYU ID', 'first name', 'last name', 'international', 'is male?', 'email', 'phone',
        'BYU ID', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name'
    ])
    student_fields = students.values_list('byu_id', 'emp_first', 'emp_last', 'international', 'is_male', 'email', 'phone')
    work_fields = works.values_list('byu_id', 'exptected_hours', 'semester', 'year', 'class_code', 'emp_record', 'supervisor_id', 
        'hire_date', 'pay_rate','last_pay_increase_date', 'pay_increase_amount', 'increase_input_date', 
        'program_year', 'is_pay_grad_tuition', 'name_change_completed','notes', 'terminated', 'termination_date', 
        'survey_sent', 'eform_submitted', 'eform_submission_date', 'auth_work_received', 'auth_work_email_sent', 'byu_name')
    for student in student_fields:
        for work in work_fields:
            if (student[0] == work[0]) and (work[2] == 'Spring') :
                writer.writerow(student+work)
    return response
