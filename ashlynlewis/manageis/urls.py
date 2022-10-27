from django.urls import path
from .views import firetablePageView, indexPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("firetable",firetablePageView,name="firetable")    
]                  
            