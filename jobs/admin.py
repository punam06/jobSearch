from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'posted_by', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'company_name', 'location')
    search_fields = ('title', 'company_name', 'location', 'description', 'posted_by__username')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job_title', 'company_name', 'status', 'applied_at', 'updated_at')
    list_filter = ('status', 'applied_at', 'updated_at', 'job__company_name')
    search_fields = ('applicant__username', 'applicant__email', 'job__title', 'job__company_name')
    readonly_fields = ('applied_at', 'updated_at')
    list_editable = ('status',)
    date_hierarchy = 'applied_at'
    
    def job_title(self, obj):
        return obj.job.title
    job_title.short_description = 'Job Title'
    
    def company_name(self, obj):
        return obj.job.company_name
    company_name.short_description = 'Company'
