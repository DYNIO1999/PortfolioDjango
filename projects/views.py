from django.shortcuts import render
from projects.models import Project
from django.http import JsonResponse
def project_index(request):

    projects = Project.objects.all()

    context = {

        'projects': projects

    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):

    project = Project.objects.get(pk=pk)

    context = {

        'project': project

    }
    return render(request, 'project_detail.html', context)


def home(request):
    
    return render(request, 'home.html')


def rate_project(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        print(val)
        obj = Project.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})