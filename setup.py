"""
Job Portal Project Setup Script

This script helps set up the Job Portal Django application with all necessary
dependencies and sample data.
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and print its description."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return None

def main():
    print("🚀 Job Portal Django Application Setup")
    print("=" * 50)
    
    # Check if virtual environment exists
    venv_path = os.path.join(os.getcwd(), 'venv')
    if not os.path.exists(venv_path):
        print("\n📦 Creating virtual environment...")
        run_command("python -m venv venv", "Virtual environment creation")
    
    # Activate virtual environment and install dependencies
    if sys.platform.startswith('win'):
        activate_cmd = "venv\\Scripts\\activate"
    else:
        activate_cmd = "source venv/bin/activate"
    
    commands = [
        (f"{activate_cmd} && pip install -r requirements.txt", "Installing dependencies"),
        (f"{activate_cmd} && python manage.py makemigrations", "Creating migrations"),
        (f"{activate_cmd} && python manage.py migrate", "Applying migrations"),
    ]
    
    for command, description in commands:
        run_command(command, description)
    
    # Create superuser (optional)
    print("\n👤 Creating superuser account...")
    superuser_script = """
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"""
    run_command(f'{activate_cmd} && echo "{superuser_script}" | python manage.py shell', "Superuser creation")
    
    # Create sample data
    run_command(f"{activate_cmd} && python manage.py create_sample_data", "Creating sample data")
    
    print("\n🎉 Setup completed successfully!")
    print("\n📝 Quick Start Guide:")
    print("1. Activate virtual environment:")
    if sys.platform.startswith('win'):
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Start development server:")
    print("   python manage.py runserver")
    print("3. Open browser and go to: http://127.0.0.1:8000/")
    print("\n🔑 Login Credentials:")
    print("   Admin: admin / admin123")
    print("   Employer: employer1 / password123")
    print("   Applicant: applicant1 / password123")

if __name__ == "__main__":
    main()
