from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    all_projects = Project.fetch_all_images()
    return render(request,"/index.html")