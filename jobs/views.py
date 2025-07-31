from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Job, Application
from .forms import JobForm, ApplicationForm, JobSearchForm
from accounts.models import UserProfile

def home(request):
    # Get search form
    form = JobSearchForm(request.GET)
    jobs = Job.objects.filter(is_active=True)
    
    # Handle search
    if form.is_valid() and form.cleaned_data['search']:
        search_query = form.cleaned_data['search']
        jobs = jobs.filter(
            Q(title__icontains=search_query) |
            Q(company_name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(jobs, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)
    
    context = {
        'jobs': jobs,
        'form': form,
        'search_query': request.GET.get('search', '')
    }
    return render(request, 'jobs/home.html', context)

def job_list(request):
    return home(request)  # Same as home

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id, is_active=True)
    user_has_applied = False
    
    if request.user.is_authenticated:
        user_has_applied = Application.objects.filter(
            job=job, applicant=request.user
        ).exists()
    
    context = {
        'job': job,
        'user_has_applied': user_has_applied
    }
    return render(request, 'jobs/job_detail.html', context)

@login_required
def post_job(request):
    # Check if user is employer
    try:
        user_profile = request.user.userprofile
        if user_profile.role != 'employer':
            messages.error(request, 'Only employers can post jobs.')
            return redirect('job_list')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Please complete your profile first.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job_detail', job_id=job.id)
    else:
        form = JobForm()
    
    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, is_active=True)
    
    # Check if user is applicant
    try:
        user_profile = request.user.userprofile
        if user_profile.role != 'applicant':
            messages.error(request, 'Only applicants can apply for jobs.')
            return redirect('job_detail', job_id=job.id)
    except UserProfile.DoesNotExist:
        messages.error(request, 'Please complete your profile first.')
        return redirect('dashboard')
    
    # Check if already applied
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('job_detail', job_id=job.id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('job_detail', job_id=job.id)
    else:
        form = ApplicationForm()
    
    context = {
        'form': form,
        'job': job
    }
    return render(request, 'jobs/apply_job.html', context)

@login_required
def job_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    applications = Application.objects.filter(job=job)
    
    context = {
        'job': job,
        'applications': applications
    }
    return render(request, 'jobs/job_applications.html', context)

@login_required
def my_jobs(request):
    # Check if user is employer
    try:
        user_profile = request.user.userprofile
        if user_profile.role != 'employer':
            messages.error(request, 'Only employers can view this page.')
            return redirect('job_list')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Please complete your profile first.')
        return redirect('dashboard')
    
    jobs = Job.objects.filter(posted_by=request.user)
    
    context = {'jobs': jobs}
    return render(request, 'jobs/my_jobs.html', context)

@login_required
def my_applications(request):
    # Check if user is applicant
    try:
        user_profile = request.user.userprofile
        if user_profile.role != 'applicant':
            messages.error(request, 'Only applicants can view this page.')
            return redirect('job_list')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Please complete your profile first.')
        return redirect('dashboard')
    
    applications = Application.objects.filter(applicant=request.user)
    
    # Filter by status if provided
    status_filter = request.GET.get('status')
    if status_filter and status_filter in ['pending', 'approved', 'rejected']:
        applications = applications.filter(status=status_filter)
    
    context = {
        'applications': applications,
        'current_filter': status_filter,
        'status_choices': Application.STATUS_CHOICES
    }
    return render(request, 'jobs/my_applications.html', context)

@login_required
@require_POST
def update_application_status(request, application_id):
    """Update the status of an application"""
    application = get_object_or_404(Application, id=application_id)
    
    # Check if user is the employer who posted the job
    if application.job.posted_by != request.user:
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    new_status = request.POST.get('status')
    if new_status not in ['approved', 'rejected']:
        return JsonResponse({'error': 'Invalid status'}, status=400)
    
    application.status = new_status
    application.save()
    
    status_text = 'Approved' if new_status == 'approved' else 'Rejected'
    return JsonResponse({
        'success': True, 
        'status': new_status,
        'status_text': status_text,
        'status_color': application.get_status_color()
    })
