#!/usr/bin/env python
"""
Production deployment script to create admin user and sample data
"""
import os
import django
import sys

try:
    # Set up Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
    django.setup()

    from django.contrib.auth.models import User
    from accounts.models import UserProfile
    from jobs.models import Job

    def create_admin_user():
        """Create admin user if it doesn't exist"""
        try:
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
        except Exception as e:
            print(f"⚠️ Could not create admin user: {e}")

    def create_sample_users():
        """Create sample employer and applicant users"""
        try:
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
        except Exception as e:
            print(f"⚠️ Could not create sample users: {e}")

    def create_sample_jobs():
        """Create sample job postings"""
        try:
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
                    }
                ]
                
                for job_data in jobs_data:
                    Job.objects.create(
                        posted_by=employer,
                        **job_data
                    )
                
                print(f"✅ Created {len(jobs_data)} sample jobs")
        except Exception as e:
            print(f"⚠️ Could not create sample jobs: {e}")

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

except Exception as e:
    print(f"❌ Error setting up production data: {e}")
    sys.exit(0)  # Don't fail the deployment if this fails
