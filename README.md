# Job Portal - Django Web Application

A comprehensive job portal web application built with Django that allows employers to post jobs and applicants to search and apply for available positions.

## 🚀 Features

### User Roles
- **Employer**: Can post jobs, view applications, and manage job listings
- **Applicant**: Can search jobs, apply with resume and cover letter, and track applications

### Authentication & Authorization
- User registration and login
- Role-based access control
- Secure logout functionality
- Dashboard redirects based on user role

### Job Management
- **For Employers:**
  - Post new job openings
  - View all posted jobs
  - Manage job applications
  - View applicant details and resumes
  
- **For Applicants:**
  - Browse all available jobs
  - Search jobs by title, company, or location
  - Apply to jobs with resume upload
  - View application history

### Search Functionality
Advanced job search capabilities:
- Search by job title
- Search by company name
- Search by location
- Real-time filtering of results

### Admin Panel
- Customized Django admin interface
- Manage users, jobs, and applications
- View detailed analytics and reports

## 🛠 Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **File Handling**: Django FileField for resume uploads
- **Authentication**: Django's built-in authentication system

## 📁 Project Structure

```
jobSearch/
├── accounts/                 # User management app
│   ├── models.py            # UserProfile model
│   ├── views.py             # Authentication views
│   ├── forms.py             # Registration forms
│   └── admin.py             # Admin configuration
├── jobs/                    # Job management app
│   ├── models.py            # Job and Application models
│   ├── views.py             # Job-related views
│   ├── forms.py             # Job and application forms
│   └── admin.py             # Admin configuration
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── accounts/           # Account templates
│   ├── jobs/               # Job templates
│   └── registration/       # Auth templates
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User uploaded files
└── manage.py               # Django management script
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd jobSearch
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Create sample data (optional)**
   ```bash
   python manage.py create_sample_data
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 👥 Sample Accounts

After running `create_sample_data`, you can use these accounts:

### Employers
- **Username**: employer1 | **Password**: password123
- **Username**: employer2 | **Password**: password123  
- **Username**: employer3 | **Password**: password123

### Applicants
- **Username**: applicant1 | **Password**: password123
- **Username**: applicant2 | **Password**: password123
- **Username**: applicant3 | **Password**: password123

### Admin
- **Username**: admin | **Password**: admin123

## 📱 Screenshots

### Home Page
- Modern, responsive design with job search functionality
- Featured job listings with pagination
- User-friendly navigation

### Job Details
- Comprehensive job information
- Apply functionality for applicants
- Application management for employers

### Dashboard
- Role-based dashboards
- Quick access to relevant features
- Statistics and overview

### Application Process
- Easy-to-use application form
- Resume upload functionality
- Cover letter submission

## 🔧 Key Features Implementation

### Models
- **UserProfile**: Extended user model with role-based permissions
- **Job**: Complete job posting model with search capabilities
- **Application**: Job application model with file upload

### Search Functionality
```python
# Advanced search with multiple fields
jobs = jobs.filter(
    Q(title__icontains=search_query) |
    Q(company_name__icontains=search_query) |
    Q(location__icontains=search_query) |
    Q(description__icontains=search_query)
)
```

### File Upload
- Secure resume upload with file validation
- Organized file storage structure
- Easy download access for employers

### Security Features
- Role-based access control
- CSRF protection
- Secure file handling
- Authentication required for sensitive operations

## 🎨 UI/UX Features

- **Responsive Design**: Works on all device sizes
- **Modern UI**: Bootstrap 5 with custom styling
- **Intuitive Navigation**: Role-based menu system
- **User Feedback**: Success/error messages
- **Clean Interface**: Professional and user-friendly

## 📊 Admin Panel Features

- **User Management**: View and manage all users
- **Job Oversight**: Monitor all job postings
- **Application Tracking**: View all applications
- **Custom List Views**: Optimized for admin tasks
- **Search and Filtering**: Easy data management

## 🚀 Deployment

### Live Demo
🌐 **[View Live Application](https://vecel1.vercel.app)** - Your Django Job Portal is now live!

### Quick Deploy to Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/punam06/jobSearch)

### Deployment Options

#### 1. Vercel (Recommended)
```bash
# Push to GitHub first
git push origin main

# Deploy to Vercel
npm install -g vercel
vercel login
vercel
```

#### 2. Manual Deployment
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions including:
- Vercel deployment (step-by-step)
- Railway deployment
- Heroku deployment
- DigitalOcean App Platform

### Environment Configuration
The application is pre-configured for deployment with:
- `vercel.json` - Vercel configuration
- `build_files.sh` - Build script
- `requirements.txt` - Dependencies
- Static files configuration
- WhiteNoise for static file serving

## 🚀 Deployment Ready

The application is ready for deployment with:
- Environment-based settings
- Static file configuration
- Media file handling
- Database configuration options

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🔮 Future Enhancements

- Email notifications for applications
- Advanced filtering options
- Job recommendation system
- Company profiles
- Application status tracking
- Interview scheduling
- Skills assessment integration

## 📞 Support

For support, email your-email@example.com or create an issue in the GitHub repository.

---

**Built with ❤️ using Django**
