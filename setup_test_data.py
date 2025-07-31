#!/usr/bin/env python
"""
Setup test data for Application Status Update Feature
This creates test employers, applicants, jobs, and applications
"""

import os
import django
from django.utils import timezone
from datetime import timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile
from jobs.models import Job, Application

def create_test_data():
    """Create test data for the application status feature"""
    print("🏗️  Setting up test data for Application Status Feature")
    print("=" * 60)
    
    # Create test employer if not exists
    employer_user, created = User.objects.get_or_create(
        username='test_employer',
        defaults={
            'email': 'employer@test.com',
            'first_name': 'Test',
            'last_name': 'Employer',
        }
    )
    if created:
        employer_user.set_password('testpass123')
        employer_user.save()
    
    employer_profile, created = UserProfile.objects.get_or_create(
        user=employer_user,
        defaults={
            'role': 'employer',
            'phone': '+1234567890',
            'location': 'San Francisco, CA',
            'bio': 'Test employer for application status feature'
        }
    )
    
    print(f"✅ Employer: {employer_user.username} ({'created' if created else 'exists'})")
    
    # Create test applicants if not exist
    applicants = []
    for i in range(3):
        applicant_user, created = User.objects.get_or_create(
            username=f'test_applicant_{i+1}',
            defaults={
                'email': f'applicant{i+1}@test.com',
                'first_name': f'Test{i+1}',
                'last_name': 'Applicant',
            }
        )
        if created:
            applicant_user.set_password('testpass123')
            applicant_user.save()
        
        applicant_profile, created = UserProfile.objects.get_or_create(
            user=applicant_user,
            defaults={
                'role': 'applicant',
                'phone': f'+123456789{i}',
                'location': f'Test City {i+1}',
                'bio': f'Test applicant {i+1} for application status feature'
            }
        )
        applicants.append(applicant_user)
        print(f"✅ Applicant: {applicant_user.username} ({'created' if created else 'exists'})")
    
    # Create test job
    test_job, created = Job.objects.get_or_create(
        title='Senior Python Developer',
        company_name='Tech Corp',
        posted_by=employer_user,
        defaults={
            'location': 'San Francisco, CA',
            'description': '''We are looking for a Senior Python Developer to join our dynamic team.
            
Requirements:
- 5+ years of Python experience
- Django framework expertise
- RESTful API development
- Database design and optimization
- Git version control
            
Benefits:
- Competitive salary
- Health insurance
- Remote work options
- Professional development budget''',
            'is_active': True,
        }
    )
    
    print(f"✅ Test Job: {test_job.title} ({'created' if created else 'exists'})")
    
    # Create test applications
    statuses = ['pending', 'pending', 'pending']  # Start with all pending
    for i, applicant in enumerate(applicants):
        application, created = Application.objects.get_or_create(
            job=test_job,
            applicant=applicant,
            defaults={
                'cover_letter': f'''Dear Hiring Manager,

I am writing to express my strong interest in the {test_job.title} position at {test_job.company_name}. 

With my background in Python development and passion for creating efficient, scalable solutions, I believe I would be a valuable addition to your team.

Key qualifications:
- Extensive Python and Django experience
- Strong problem-solving skills
- Excellent communication and teamwork abilities
- Commitment to continuous learning and improvement

I would welcome the opportunity to discuss how my skills and experience can contribute to your team's success.

Best regards,
{applicant.get_full_name() or applicant.username}''',
                'status': statuses[i],
            }
        )
        print(f"✅ Application: {applicant.username} -> {test_job.title} ({'created' if created else 'exists'})")
    
    print("\n📊 Current Application Status Distribution:")
    for status_value, status_label in Application.STATUS_CHOICES:
        count = Application.objects.filter(status=status_value).count()
        print(f"   {status_label}: {count}")
    
    print(f"\n🎯 Test URLs to visit:")
    print(f"   👨‍💼 Employer Dashboard: http://127.0.0.1:8000/accounts/dashboard/")
    print(f"   📋 Job Applications: http://127.0.0.1:8000/jobs/{test_job.id}/applications/")
    print(f"   👩‍💻 My Applications: http://127.0.0.1:8000/my-applications/")
    print(f"   🏠 Home: http://127.0.0.1:8000/")
    
    print(f"\n🔑 Test Login Credentials:")
    print(f"   Employer: test_employer / testpass123")
    print(f"   Applicants: test_applicant_1, test_applicant_2, test_applicant_3 / testpass123")
    
    print("\n🎉 Test data setup complete!")
    print("=" * 60)

if __name__ == "__main__":
    create_test_data()
