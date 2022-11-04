from django.urls import path
from .views import firetablePageView, indexPageView, deleteEmployeePageView, updateSingleStudent, editSingleStudent, sup_export_to_csv,stud_export_to_csv,summer_export_to_csv, spring_export_to_csv, fall_export_to_csv,winter_export_to_csv

urlpatterns = [
    path("", indexPageView, name="index"),
    path("firetable",firetablePageView,name="firetable"),
    path("deleteEmployee/<int:byu_id>", deleteEmployeePageView, name="deleteEmployee"),
    path("editsinglestudent/<int:byu_id>", editSingleStudent, name="editsinglestudent"),
    path("updatesinglestudent", updateSingleStudent, name="updatesinglestudent"),
    path("sup_export_to_csv", sup_export_to_csv, name="sup_export_to_csv"),
    path("stud_export_to_csv", stud_export_to_csv, name="stud_export_to_csv"),
    path("summer_export_to_csv", summer_export_to_csv, name="summer_export_to_csv"),
    path("spring_export_to_csv", spring_export_to_csv, name="spring_export_to_csv"),
    path("fall_export_to_csv", fall_export_to_csv, name="fall_export_to_csv"),
    path("winter_export_to_csv", winter_export_to_csv, name="winter_export_to_csv"),

]                  
            