from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Service
from .forms import ServiceCreateForm


def service_list_view(request):
    """
    Barcha service'larni ko‘rsatadi
    (login shart emas)
    """
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {
        'services': services
    })


def service_detail_view(request, pk):
    """
    Bitta service detail sahifasi
    """
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {
        'service': service
    })


@login_required
def service_create_view(request):
    """
    Service yaratish
    Faqat freelancer yoki both
    """
    profile = request.user.profile

    # role tekshiruvi
    if profile.role not in ['freelancer', 'both']:
        return redirect('service_list')

    if request.method == 'POST':
        form = ServiceCreateForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.owner = profile  # MUHIM
            service.save()
            form.save_m2m()  # skills uchun
            return redirect('service_list')
    else:
        form = ServiceCreateForm()

    return render(request, 'services/service_create.html', {
        'form': form
    })


@login_required
def service_my_list_view(request):
    """
    Faqat user'ning o‘z service'lari
    """
    profile = request.user.profile
    services = Service.objects.filter(owner=profile)

    return render(request, 'services/service_my_list.html', {
        'services': services
    })
