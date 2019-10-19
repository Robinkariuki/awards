from django.shortcuts import render,redirect
from .models import Project,profile
from .forms import ProjectForm,VoteForm
# Create your views here.
def home(request):
    all_projects = Project.fetch_all_images()
    return render(request,"index.html",{"all_images":all_projects})





def project_review(request,project_id):
    try:
        single_project = Project.get_single_project(project_id)
        average_score = round(((single_project.design + single_project.usability + single_project.content)/3),2)
        if request.method == 'POST':
            vote_form = VoteForm(request.POST)
            if vote_form.is_valid():
                single_project.vote_submissions+=1
                if single_project.design == 0:
                    single_project.design = int(request.POST['design'])
                else:
                    single_project.design = (single_project.design + int(request.POST['design']))/2
                if single_project.usability == 0:
                    single_project.usability = int(request.POST['usability'])
                else:
                    single_project.usability = (single_project.usability + int(request.POST['usability']))/2
                if single_project.content == 0:
                    single_project.content = int(request.POST['content'])
                else:
                    single_project.content = (single_project.content + int(request.POST['usability']))/2

                single_project.save()
                return redirect('project_review',project_id)
        else:
            vote_form = VoteForm()

    except Exception as  e:
        raise Http404()
    return render(request,'project_review.html',{"vote_form":vote_form,"single_project":single_project,"average_score":average_score})   

def search_project(request):
    if 'project' in request.GET and request.GET ["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {"message":message, "projects":searched_projects})

    else:
        message = "No search results yet!"
        return render (request, 'search.html', {"message": message})

def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile/profile.html',{'profile':prof,'projects':projects})        