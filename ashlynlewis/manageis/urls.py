from django.urls import path
from .views import firetablePageView, indexPageView, deleteEmployeePageView, updateSingleStudent, editSingleStudent

urlpatterns = [
    path("", indexPageView, name="index"),
    path("firetable",firetablePageView,name="firetable"),
    path("deleteEmployee/<int:byu_id>", deleteEmployeePageView, name="deleteEmployee"),
    
    path("editsinglestudent/<int:byu_id>", editSingleStudent, name="editsinglestudent"),
    path("updatesinglestudent", updateSingleStudent, name="updatesinglestudent"),

]                  
            