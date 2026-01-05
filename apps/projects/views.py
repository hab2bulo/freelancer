from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectCreateForm


def project_list_view(request):
    """
    Hamma ochiq projectlar ro‘yxati
    """
    projects = Project.objects.filter(is_open=True)
    return render(request, 'projects/project_list.html', {
        'projects': projects
    })


def project_detail_view(request, pk):
    """
    Bitta project sahifasi
    """
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {
        'project': project
    })


@login_required
def project_create_view(request):
    """
    Project yaratish (faqat client yoki both)
    """
    profile = request.user.profile

    # role tekshiruvi
    if profile.role not in ['client', 'both']:
        return redirect('project_list')

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = profile
            project.save()
            return redirect('project_list')
    else:
        form = ProjectCreateForm()

    return render(request, 'projects/project_create.html', {
        'form': form
    })
