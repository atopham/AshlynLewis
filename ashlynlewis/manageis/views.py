from django.shortcuts import render

# Create your views here.
def indexPageView(request) :
    return render(request, 'manageis/index.html')
def firetablePageView(request) :
    return render(request, 'manageis/firetable.html') 