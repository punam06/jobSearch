from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import UserProfile
from jobs.models import Job
import random

class Command(BaseCommand):
    help = 'Create sample data for the job portal'

    def handle(self, *args, **options):
        # Create sample employers
        employers_data = [
            {'username': 'employer1', 'email': 'employer1@example.com', 'first_name': 'John', 'last_name': 'Smith', 'company': 'TechCorp Inc.'},
            {'username': 'employer2', 'email': 'employer2@example.com', 'first_name': 'Sarah', 'last_name': 'Johnson', 'company': 'InnovateLab'},
            {'username': 'employer3', 'email': 'employer3@example.com', 'first_name': 'Michael', 'last_name': 'Brown', 'company': 'DataSystems Ltd.'},
        ]

        # Create sample applicants
        applicants_data = [
            {'username': 'applicant1', 'email': 'applicant1@example.com', 'first_name': 'Alice', 'last_name': 'Williams'},
            {'username': 'applicant2', 'email': 'applicant2@example.com', 'first_name': 'Bob', 'last_name': 'Davis'},
            {'username': 'applicant3', 'email': 'applicant3@example.com', 'first_name': 'Carol', 'last_name': 'Wilson'},
        ]

        # Create employers
        employers = []
        for emp_data in employers_data:
            if not User.objects.filter(username=emp_data['username']).exists():
                user = User.objects.create_user(
                    username=emp_data['username'],
                    email=emp_data['email'],
                    password='password123',
                    first_name=emp_data['first_name'],
                    last_name=emp_data['last_name']
                )
                UserProfile.objects.create(
                    user=user,
                    role='employer',
                    phone=f'+1-555-{random.randint(1000, 9999)}',
                    location='New York, NY',
                    bio=f'HR Manager at {emp_data["company"]}'
                )
                employers.append(user)
                self.stdout.write(f'Created employer: {user.username}')

        # Create applicants
        applicants = []
        for app_data in applicants_data:
            if not User.objects.filter(username=app_data['username']).exists():
                user = User.objects.create_user(
                    username=app_data['username'],
                    email=app_data['email'],
                    password='password123',
                    first_name=app_data['first_name'],
                    last_name=app_data['last_name']
                )
                UserProfile.objects.create(
                    user=user,
                    role='applicant',
                    phone=f'+1-555-{random.randint(1000, 9999)}',
                    location=random.choice(['San Francisco, CA', 'Seattle, WA', 'Austin, TX', 'Boston, MA']),
                    bio=f'Experienced professional looking for new opportunities.'
                )
                applicants.append(user)
                self.stdout.write(f'Created applicant: {user.username}')

        # Create sample jobs
        jobs_data = [
            {
                'title': 'Senior Software Engineer',
                'company_name': 'TechCorp Inc.',
                'location': 'San Francisco, CA',
                'description': '''We are looking for a Senior Software Engineer to join our dynamic team. 

Responsibilities:
• Design and develop scalable web applications
• Collaborate with cross-functional teams
• Mentor junior developers
• Participate in code reviews

Requirements:
• 5+ years of experience in software development
• Strong knowledge of Python, JavaScript, and React
• Experience with cloud platforms (AWS, Azure)
• Excellent problem-solving skills
• Bachelor's degree in Computer Science or related field

We offer competitive salary, health benefits, and flexible work arrangements.'''
            },
            {
                'title': 'Data Scientist',
                'company_name': 'InnovateLab',
                'location': 'Seattle, WA',
                'description': '''Join our data science team to work on cutting-edge machine learning projects.

Responsibilities:
• Develop predictive models and algorithms
• Analyze large datasets to extract insights
• Present findings to stakeholders
• Collaborate with engineering teams

Requirements:
• Master's degree in Data Science, Statistics, or related field
• 3+ years of experience in data science
• Proficiency in Python, R, and SQL
• Experience with machine learning frameworks
• Strong communication skills

Benefits include stock options, professional development budget, and remote work flexibility.'''
            },
            {
                'title': 'Product Manager',
                'company_name': 'DataSystems Ltd.',
                'location': 'Austin, TX',
                'description': '''We're seeking a Product Manager to drive our product strategy and roadmap.

Responsibilities:
• Define product vision and strategy
• Work with engineering and design teams
• Conduct market research and user interviews
• Manage product roadmap and backlog

Requirements:
• 4+ years of product management experience
• Strong analytical and problem-solving skills
• Experience with agile development methodologies
• Excellent communication and leadership skills
• MBA or equivalent experience preferred

Join us to shape the future of data management solutions!'''
            },
            {
                'title': 'Frontend Developer',
                'company_name': 'TechCorp Inc.',
                'location': 'Remote',
                'description': '''Looking for a Frontend Developer to create amazing user experiences.

Responsibilities:
• Build responsive web applications
• Implement modern UI/UX designs
• Optimize application performance
• Collaborate with backend developers

Requirements:
• 3+ years of frontend development experience
• Expert knowledge of React, TypeScript, and CSS
• Experience with modern build tools
• Understanding of web accessibility
• Portfolio demonstrating your work

This is a fully remote position with occasional team meetups.'''
            },
            {
                'title': 'DevOps Engineer',
                'company_name': 'InnovateLab',
                'location': 'Boston, MA',
                'description': '''Join our DevOps team to build and maintain our infrastructure.

Responsibilities:
• Design and implement CI/CD pipelines
• Manage cloud infrastructure (AWS/Azure)
• Monitor system performance and reliability
• Automate deployment processes

Requirements:
• 4+ years of DevOps experience
• Strong knowledge of containerization (Docker, Kubernetes)
• Experience with infrastructure as code (Terraform)
• Proficiency in scripting languages
• AWS or Azure certifications preferred

We offer excellent benefits and opportunities for professional growth.'''
            }
        ]

        # Get existing employers for job assignment
        existing_employers = User.objects.filter(userprofile__role='employer')
        
        for job_data in jobs_data:
            # Find the employer based on company name
            employer = None
            for emp in existing_employers:
                if job_data['company_name'] in emp.userprofile.bio or job_data['company_name'] == 'TechCorp Inc.' and emp.username == 'employer1':
                    employer = emp
                    break
                elif job_data['company_name'] == 'InnovateLab' and emp.username == 'employer2':
                    employer = emp
                    break
                elif job_data['company_name'] == 'DataSystems Ltd.' and emp.username == 'employer3':
                    employer = emp
                    break
            
            if not employer:
                employer = existing_employers.first()
            
            if employer and not Job.objects.filter(title=job_data['title'], company_name=job_data['company_name']).exists():
                Job.objects.create(
                    title=job_data['title'],
                    company_name=job_data['company_name'],
                    location=job_data['location'],
                    description=job_data['description'],
                    posted_by=employer
                )
                self.stdout.write(f'Created job: {job_data["title"]} at {job_data["company_name"]}')

        self.stdout.write(self.style.SUCCESS('Successfully created sample data!'))
