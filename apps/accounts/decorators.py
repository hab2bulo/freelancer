from django.shortcuts import redirect

def freelancer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.profile.role in ['freelancer', 'both']:
            return view_func(request, *args, **kwargs)
        return redirect('profile')
    return wrapper
