from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def demo_home(request):
    """Demo home page matching original Django template design"""
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home - Job Portal</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <style>
            .navbar-brand {
                font-weight: bold;
                color: #007bff !important;
            }
            .job-card {
                transition: transform 0.2s;
                border: 1px solid #dee2e6;
            }
            .job-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            .footer {
                background-color: #343a40;
                color: white;
                padding: 20px 0;
                margin-top: 50px;
            }
            .hero-section {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 60px 0;
            }
            .btn-primary {
                background-color: #667eea;
                border-color: #667eea;
            }
            .btn-primary:hover {
                background-color: #5a6fd8;
                border-color: #5a6fd8;
            }
            .demo-notice {
                background: #fff3cd;
                border: 1px solid #ffeaa7;
                color: #856404;
                padding: 10px 15px;
                border-radius: 5px;
                margin: 10px 0;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm">
            <div class="container">
                <a class="navbar-brand" href="/">
                    <i class="fas fa-briefcase me-2"></i>JobPortal
                </a>
                
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="/">
                                <i class="fas fa-home me-1"></i>Home
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/jobs/">
                                <i class="fas fa-search me-1"></i>Browse Jobs
                            </a>
                        </li>
                    </ul>
                    
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="/accounts/login/">
                                <i class="fas fa-sign-in-alt me-1"></i>Login
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/accounts/register/">
                                <i class="fas fa-user-plus me-1"></i>Register
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Demo Notice -->
        <div class="container mt-3">
            <div class="demo-notice">
                <strong>📢 Demo Mode:</strong> This is a static demo deployed on Vercel. 
                For full functionality with user authentication and database features, 
                run locally or deploy with PostgreSQL.
            </div>
        </div>

        <!-- Hero Section -->
        <section class="hero-section">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6">
                        <h1 class="display-4 fw-bold mb-4">Find Your Dream Job</h1>
                        <p class="lead mb-4">Connect with top employers and discover opportunities that match your skills and aspirations.</p>
                        <div class="d-flex gap-3">
                            <a href="/jobs/" class="btn btn-light btn-lg">Browse Jobs</a>
                            <a href="/accounts/register/" class="btn btn-outline-light btn-lg">Join Now</a>
                        </div>
                    </div>
                    <div class="col-lg-6 text-center">
                        <i class="fas fa-search-location" style="font-size: 8rem; opacity: 0.3;"></i>
                    </div>
                </div>
            </div>
        </section>

        <!-- Search Section -->
        <section class="py-5">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-8">
                        <div class="card shadow">
                            <div class="card-body p-4">
                                <h3 class="text-center mb-4">Search Jobs</h3>
                                <form method="GET" action="/jobs/">
                                    <div class="input-group input-group-lg">
                                        <input type="text" class="form-control" placeholder="Enter job title, company, or keywords..." name="search">
                                        <button class="btn btn-primary" type="submit">
                                            <i class="fas fa-search me-2"></i>Search
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Latest Jobs Section -->
        <section class="py-5 bg-light">
            <div class="container">
                <h2 class="text-center mb-5">Latest Job Opportunities</h2>
                
                <div class="text-center">
                    <div class="py-5">
                        <i class="fas fa-search" style="font-size: 4rem; color: #dee2e6;"></i>
                        <h4 class="mt-3 text-muted">No jobs found</h4>
                        <p class="text-muted">No jobs have been posted yet.</p>
                        <a href="/post-job/" class="btn btn-primary mt-3">Post the First Job</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Stats Section -->
        <section class="py-5">
            <div class="container">
                <div class="row text-center">
                    <div class="col-md-4">
                        <div class="card border-0">
                            <div class="card-body">
                                <i class="fas fa-briefcase fa-3x text-primary mb-3"></i>
                                <h3 class="text-primary">0</h3>
                                <p class="text-muted">Active Jobs</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card border-0">
                            <div class="card-body">
                                <i class="fas fa-building fa-3x text-success mb-3"></i>
                                <h3 class="text-success">50+</h3>
                                <p class="text-muted">Companies</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card border-0">
                            <div class="card-body">
                                <i class="fas fa-users fa-3x text-info mb-3"></i>
                                <h3 class="text-info">1000+</h3>
                                <p class="text-muted">Job Seekers</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="footer mt-auto">
            <div class="container">
                <div class="row">
                    <div class="col-md-6">
                        <h5><i class="fas fa-briefcase me-2"></i>JobPortal</h5>
                        <p>Find your dream job or hire the perfect candidate.</p>
                    </div>
                    <div class="col-md-6 text-md-end">
                        <p>&copy; 2025 JobPortal. All rights reserved.</p>
                        <div class="social-links">
                            <a href="#" class="text-white me-3"><i class="fab fa-facebook"></i></a>
                            <a href="#" class="text-white me-3"><i class="fab fa-twitter"></i></a>
                            <a href="#" class="text-white"><i class="fab fa-linkedin"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """)

@csrf_exempt
def demo_view(request):
    """Generic demo view matching original Django template design"""
    page_name = request.path.strip('/').replace('/', ' - ').title() or 'Home'
    
    # Determine page-specific content
    page_content = ""
    if 'jobs' in request.path:
        page_content = """
        <div class="py-3">
            <h2 class="mb-4">Browse Jobs</h2>
            
            <!-- Search Bar -->
            <div class="row justify-content-center mb-4">
                <div class="col-lg-8">
                    <div class="card">
                        <div class="card-body p-3">
                            <form method="GET">
                                <div class="input-group">
                                    <input type="text" class="form-control" placeholder="Search jobs by title, company, or location..." name="search">
                                    <button class="btn btn-primary" type="submit">
                                        <i class="fas fa-search me-2"></i>Search
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>

            <!-- No Jobs Found -->
            <div class="text-center py-5">
                <i class="fas fa-search" style="font-size: 4rem; color: #dee2e6;"></i>
                <h4 class="mt-3 text-muted">No jobs found</h4>
                <p class="text-muted">No jobs have been posted yet.</p>
                <a href="/post-job/" class="btn btn-primary mt-3">Post the First Job</a>
            </div>
        </div>
        """
    elif 'register' in request.path:
        page_content = """
        <div class="row justify-content-center">
            <div class="col-lg-6">
                <div class="card shadow">
                    <div class="card-body p-5">
                        <div class="text-center mb-4">
                            <h2 class="text-primary">
                                <i class="fas fa-user-plus me-2"></i>Create Account
                            </h2>
                            <p class="text-muted">Join our job portal to find opportunities or hire talent</p>
                        </div>
                        
                        <form>
                            <div class="row">
                                <div class="col-md-6 mb-3">
                                    <label class="form-label">
                                        <i class="fas fa-user me-1"></i>First Name
                                    </label>
                                    <input type="text" class="form-control" placeholder="First name" required>
                                </div>
                                <div class="col-md-6 mb-3">
                                    <label class="form-label">
                                        <i class="fas fa-user me-1"></i>Last Name
                                    </label>
                                    <input type="text" class="form-control" placeholder="Last name" required>
                                </div>
                            </div>
                            
                            <div class="mb-3">
                                <label class="form-label">
                                    <i class="fas fa-at me-1"></i>Username
                                </label>
                                <input type="text" class="form-control" placeholder="Choose a username" required>
                            </div>
                            
                            <div class="mb-3">
                                <label class="form-label">
                                    <i class="fas fa-envelope me-1"></i>Email
                                </label>
                                <input type="email" class="form-control" placeholder="Enter your email" required>
                            </div>
                            
                            <div class="mb-3">
                                <label class="form-label">
                                    <i class="fas fa-briefcase me-1"></i>I am a
                                </label>
                                <select class="form-select" required>
                                    <option value="">Select your role</option>
                                    <option value="applicant">Job Seeker</option>
                                    <option value="employer">Employer</option>
                                </select>
                            </div>
                            
                            <div class="row">
                                <div class="col-md-6 mb-3">
                                    <label class="form-label">
                                        <i class="fas fa-phone me-1"></i>Phone (Optional)
                                    </label>
                                    <input type="text" class="form-control" placeholder="Phone number">
                                </div>
                                <div class="col-md-6 mb-3">
                                    <label class="form-label">
                                        <i class="fas fa-map-marker-alt me-1"></i>Location (Optional)
                                    </label>
                                    <input type="text" class="form-control" placeholder="City, State">
                                </div>
                            </div>
                            
                            <div class="mb-3">
                                <label class="form-label">
                                    <i class="fas fa-info-circle me-1"></i>Bio (Optional)
                                </label>
                                <textarea class="form-control" rows="3" placeholder="Tell us about yourself..."></textarea>
                            </div>
                            
                            <div class="mb-3">
                                <label class="form-label">
                                    <i class="fas fa-lock me-1"></i>Password
                                </label>
                                <input type="password" class="form-control" placeholder="Create a password" required>
                            </div>
                            
                            <div class="mb-4">
                                <label class="form-label">
                                    <i class="fas fa-lock me-1"></i>Confirm Password
                                </label>
                                <input type="password" class="form-control" placeholder="Confirm your password" required>
                            </div>
                            
                            <button type="submit" class="btn btn-primary btn-lg w-100 mb-3">
                                <i class="fas fa-user-plus me-2"></i>Create Account
                            </button>
                            
                            <div class="text-center">
                                <p class="mb-0">Already have an account? 
                                    <a href="/accounts/login/" class="text-decoration-none">Sign in here</a>
                                </p>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        """
    elif 'login' in request.path:
        page_content = """
        <div class="row justify-content-center">
            <div class="col-lg-5">
                <div class="card shadow">
                    <div class="card-body p-5">
                        <div class="text-center mb-4">
                            <h2 class="text-primary">
                                <i class="fas fa-sign-in-alt me-2"></i>Welcome Back
                            </h2>
                            <p class="text-muted">Sign in to your account</p>
                        </div>
                        
                        <form>
                            <div class="mb-3">
                                <label class="form-label">
                                    <i class="fas fa-user me-1"></i>Username
                                </label>
                                <input type="text" class="form-control form-control-lg" placeholder="Enter your username" required>
                            </div>
                            
                            <div class="mb-4">
                                <label class="form-label">
                                    <i class="fas fa-lock me-1"></i>Password
                                </label>
                                <input type="password" class="form-control form-control-lg" placeholder="Enter your password" required>
                            </div>
                            
                            <button type="submit" class="btn btn-primary btn-lg w-100 mb-3">
                                <i class="fas fa-sign-in-alt me-2"></i>Sign In
                            </button>
                            
                            <div class="text-center">
                                <p class="mb-0">Don't have an account? 
                                    <a href="/accounts/register/" class="text-decoration-none">Create one here</a>
                                </p>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        """
    elif 'post-job' in request.path:
        page_content = """
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card shadow">
                    <div class="card-body p-5">
                        <div class="text-center mb-4">
                            <h2 class="text-primary">
                                <i class="fas fa-plus-circle me-2"></i>Post a New Job
                            </h2>
                            <p class="text-muted">Fill out the details to attract the right candidates</p>
                        </div>
                        
                        <form>
                            <div class="mb-3">
                                <label class="form-label">
                                    <i class="fas fa-briefcase me-1"></i>Job Title *
                                </label>
                                <input type="text" class="form-control" placeholder="e.g. Senior Python Developer" style="border: 2px solid #e9ecef; border-radius: 8px; padding: 12px 16px; font-size: 1rem;">
                                <div class="form-text">Enter a clear, descriptive job title</div>
                            </div>
                            
                            <div class="mb-3">
                                <label class="form-label">
                                    <i class="fas fa-building me-1"></i>Company Name *
                                </label>
                                <input type="text" class="form-control" placeholder="Your company name" style="border: 2px solid #e9ecef; border-radius: 8px; padding: 12px 16px; font-size: 1rem;">
                            </div>
                            
                            <div class="mb-3">
                                <label class="form-label">
                                    <i class="fas fa-map-marker-alt me-1"></i>Location *
                                </label>
                                <input type="text" class="form-control" placeholder="City, State or Remote" style="border: 2px solid #e9ecef; border-radius: 8px; padding: 12px 16px; font-size: 1rem;">
                                <div class="form-text">City, State or Remote</div>
                            </div>
                            
                            <div class="mb-4">
                                <label class="form-label">
                                    <i class="fas fa-file-alt me-1"></i>Job Description *
                                </label>
                                <textarea class="form-control" rows="8" placeholder="Include job responsibilities, requirements, qualifications, and any other relevant information..." style="border: 2px solid #e9ecef; border-radius: 8px; padding: 12px 16px; font-size: 1rem; min-height: 150px; resize: vertical;"></textarea>
                                <div class="form-text">
                                    Include job responsibilities, requirements, qualifications, and any other relevant information
                                </div>
                            </div>
                            
                            <div class="d-flex gap-3">
                                <button type="submit" class="btn btn-primary btn-lg">
                                    <i class="fas fa-paper-plane me-2"></i>Post Job
                                </button>
                                <a href="/jobs/" class="btn btn-outline-secondary btn-lg">
                                    <i class="fas fa-times me-2"></i>Cancel
                                </a>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        """
    
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{page_name} - Job Portal</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <style>
            .navbar-brand {{
                font-weight: bold;
                color: #007bff !important;
            }}
            .job-card {{
                transition: transform 0.2s;
                border: 1px solid #dee2e6;
            }}
            .job-card:hover {{
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}
            .footer {{
                background-color: #343a40;
                color: white;
                padding: 20px 0;
                margin-top: 50px;
            }}
            .btn-primary {{
                background-color: #667eea;
                border-color: #667eea;
            }}
            .btn-primary:hover {{
                background-color: #5a6fd8;
                border-color: #5a6fd8;
            }}
            .demo-notice {{
                background: #fff3cd;
                border: 1px solid #ffeaa7;
                color: #856404;
                padding: 10px 15px;
                border-radius: 5px;
                margin: 10px 0;
                font-size: 0.9em;
            }}
            .page-header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 60px 0;
            }}
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm">
            <div class="container">
                <a class="navbar-brand" href="/">
                    <i class="fas fa-briefcase me-2"></i>JobPortal
                </a>
                
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="/">
                                <i class="fas fa-home me-1"></i>Home
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/jobs/">
                                <i class="fas fa-search me-1"></i>Browse Jobs
                            </a>
                        </li>
                    </ul>
                    
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="/accounts/login/">
                                <i class="fas fa-sign-in-alt me-1"></i>Login
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/accounts/register/">
                                <i class="fas fa-user-plus me-1"></i>Register
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Demo Notice -->
        <div class="container mt-3">
            <div class="demo-notice">
                <strong>📢 Demo Mode:</strong> This is a static demo page. 
                In a full deployment, this would be a functional {page_name.lower()} page 
                with user authentication, database integration, and full CRUD operations.
            </div>
        </div>

        <!-- Page Header -->
        <section class="page-header">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12 text-center">
                        <h1 class="display-5 fw-bold">{page_name}</h1>
                        <p class="lead">Experience the full functionality of our Django job portal</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Main Content -->
        <section class="py-5">
            <div class="container">
                {page_content}
                
                {("" if page_content else f"""
                <div class="text-center">
                    <div class="row justify-content-center">
                        <div class="col-lg-8">
                            <div class="card border-0 shadow-sm">
                                <div class="card-body p-5">
                                    <h3 class="mb-4">🔧 What this page would normally do:</h3>
                                    <div class="text-start">
                                        <p><strong>🏠 Home:</strong> Display featured jobs, search functionality, and recent postings</p>
                                        <p><strong>💼 Jobs:</strong> Browse all available jobs with filtering and pagination</p>
                                        <p><strong>👤 Register:</strong> User registration with email verification</p>
                                        <p><strong>🔐 Login:</strong> User authentication and session management</p>
                                        <p><strong>📝 Post Job:</strong> Employers can post new job listings</p>
                                        <p><strong>📋 Applications:</strong> Track job applications and status</p>
                                    </div>
                                    
                                    <div class="mt-4">
                                        <a href="/" class="btn btn-primary me-2">🏠 Back to Home</a>
                                        <a href="/jobs/" class="btn btn-outline-primary">💼 Browse Jobs</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                """)}
            </div>
        </section>

        <!-- Footer -->
        <footer class="footer mt-auto">
            <div class="container">
                <div class="row">
                    <div class="col-md-6">
                        <h5><i class="fas fa-briefcase me-2"></i>JobPortal</h5>
                        <p>Find your dream job or hire the perfect candidate.</p>
                    </div>
                    <div class="col-md-6 text-md-end">
                        <p>&copy; 2025 JobPortal. All rights reserved.</p>
                        <div class="social-links">
                            <a href="#" class="text-white me-3"><i class="fab fa-facebook"></i></a>
                            <a href="#" class="text-white me-3"><i class="fab fa-twitter"></i></a>
                            <a href="#" class="text-white"><i class="fab fa-linkedin"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """)
