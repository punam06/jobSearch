#!/usr/bin/env python
"""
Production deployment script to create admin user and sample data
"""
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile
from jobs.models import Job

def create_admin_user():
    """Create admin user if it doesn't exist"""
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@jobportal.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print("✅ Admin user created: admin/admin123")
    else:
        print("✅ Admin user already exists")

def create_sample_users():
    """Create sample employer and applicant users"""
    # Create employer
    if not User.objects.filter(username='employer1').exists():
        employer = User.objects.create_user(
            username='employer1',
            email='employer@company.com',
            password='password123',
            first_name='John',
            last_name='Smith'
        )
        UserProfile.objects.create(
            user=employer,
            role='employer',
            phone='(555) 123-4567',
            location='San Francisco, CA',
            bio='HR Manager at TechCorp'
        )
        print("✅ Sample employer created: employer1/password123")
    
    # Create applicant
    if not User.objects.filter(username='applicant1').exists():
        applicant = User.objects.create_user(
            username='applicant1',
            email='applicant@email.com',
            password='password123',
            first_name='Jane',
            last_name='Doe'
        )
        UserProfile.objects.create(
            user=applicant,
            role='applicant',
            phone='(555) 987-6543',
            location='New York, NY',
            bio='Software Developer looking for new opportunities'
        )
        print("✅ Sample applicant created: applicant1/password123")

def create_sample_jobs():
    """Create sample job postings"""
    if User.objects.filter(username='employer1').exists() and Job.objects.count() == 0:
        employer = User.objects.get(username='employer1')
        
        jobs_data = [
            {
                'title': 'Senior Python Developer',
                'company_name': 'TechCorp Solutions',
                'location': 'San Francisco, CA',
                'description': '''We are seeking an experienced Python Developer to join our growing team. 

Key Responsibilities:
• Develop and maintain web applications using Django
• Write clean, maintainable, and efficient code
• Collaborate with cross-functional teams
• Participate in code reviews and technical discussions

Requirements:
• 5+ years of Python development experience
• Strong knowledge of Django framework
• Experience with PostgreSQL and RESTful APIs
• Knowledge of Git version control
• Excellent problem-solving skills

Benefits:
• Competitive salary ($120,000 - $150,000)
• Health, dental, and vision insurance
• 401(k) with company matching
• Flexible work arrangements
• Professional development opportunities'''
            },
            {
                'title': 'Frontend React Developer',
                'company_name': 'StartupX',
                'location': 'Remote',
                'description': '''Join our dynamic startup as a Frontend Developer!

What You'll Do:
• Build responsive web applications using React
• Collaborate with designers to implement UI/UX designs
• Optimize applications for maximum speed and scalability
• Participate in agile development processes

Requirements:
• 3+ years of React development experience
• Proficiency in JavaScript, HTML5, and CSS3
• Experience with state management (Redux, Context API)
• Knowledge of modern build tools (Webpack, Babel)
• Understanding of RESTful APIs

What We Offer:
• Competitive salary ($90,000 - $120,000)
• Equity package
• Remote-first culture
• Flexible hours
• Annual company retreat'''
            }
        ]
        
        for job_data in jobs_data:
            Job.objects.create(
                posted_by=employer,
                **job_data
            )
        
        print(f"✅ Created {len(jobs_data)} sample jobs")

if __name__ == '__main__':
    print("🚀 Setting up production data...")
    create_admin_user()
    create_sample_users()
    create_sample_jobs()
    print("✅ Production setup complete!")
    print("\n📝 Login Credentials:")
    print("🔹 Admin: admin/admin123")
    print("🔹 Employer: employer1/password123") 
    print("🔹 Applicant: applicant1/password123")
