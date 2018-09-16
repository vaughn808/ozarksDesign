from django.shortcuts import render

# Create your views here.
def home(request):
    # this is the home page view Function
    return render(request, 'home.html')

def campus(request):
    # this is the home page view Function
    return render(request, 'campus.html')

def schedule(request):
    # this is the home page view Function
    return render(request, 'schedule.html')

def about(request):
    # this is the home page view Function
    return render(request, 'about.html')
