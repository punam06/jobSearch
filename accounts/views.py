from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Create a default profile if it doesn't exist
        user_profile = UserProfile.objects.create(
            user=request.user,
            role='applicant'  # default role
        )
    
    context = {'user_profile': user_profile}
    
    if user_profile.role == 'employer':
        from jobs.models import Job
        jobs_posted = Job.objects.filter(posted_by=request.user)
        context['jobs_posted'] = jobs_posted
        return render(request, 'accounts/employer_dashboard.html', context)
    else:
        from jobs.models import Application
        applications = Application.objects.filter(applicant=request.user)
        context['applications'] = applications
        return render(request, 'accounts/applicant_dashboard.html', context)
