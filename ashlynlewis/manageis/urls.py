from django.urls import path
from .views import firetablePageView, indexPageView, deleteEmployeePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("firetable",firetablePageView,name="firetable"),
    path("deleteEmployee/<int:byu_id>", deleteEmployeePageView, name="deleteEmployee")
    
]                  
            