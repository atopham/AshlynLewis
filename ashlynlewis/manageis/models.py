# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class StudentEmployee(models.Model):
    byu_id = models.IntegerField(primary_key=True)
    emp_first = models.CharField(max_length=20)
    emp_last = models.CharField(max_length=20)
    position = models.CharField(max_length =50, blank=True, null=True)
    international = models.BooleanField()
    is_male = models.BooleanField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_employee'


class StudentWork(models.Model):
    byu_id = models.IntegerField(primary_key=True)
    exptected_hours = models.SmallIntegerField(blank=True, null=True)
    semester = models.CharField(max_length=10, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    class_code = models.CharField(max_length=50, blank=True, null=True)
    emp_record = models.CharField(max_length=50, blank=True, null=True)
    supervisor = models.ForeignKey('Supervisor', models.DO_NOTHING, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    pay_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_pay_increase_date = models.DateField(blank=True, null=True)
    pay_increase_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    increase_input_date = models.DateField(blank=True, null=True)
    program_year = models.CharField(max_length=50, blank=True, null=True)
    is_pay_grad_tuition = models.BooleanField(blank=True, null=True)
    name_change_completed = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    terminated = models.BooleanField(blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    survey_sent = models.BooleanField(blank=True, null=True)
    eform_submitted = models.BooleanField(blank=True, null=True)
    eform_submission_date = models.DateField(blank=True, null=True)
    auth_work_received = models.BooleanField(blank=True, null=True)
    auth_work_email_sent = models.DateField(blank=True, null=True)
    byu_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_work'


class Supervisor(models.Model):
    supervisor_id = models.IntegerField(primary_key=True)
    supervisor_first = models.CharField(max_length=50)
    supervisor_last = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'supervisor'
