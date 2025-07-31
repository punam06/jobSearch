from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def demo_home(request):
    """Demo home page for Vercel deployment"""
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Job Portal - Demo</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 0; 
                padding: 20px; 
                background-color: #f5f5f5; 
            }
            .container { 
                max-width: 1200px; 
                margin: 0 auto; 
                background: white; 
                padding: 20px; 
                border-radius: 8px; 
                box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
            }
            .header { 
                text-align: center; 
                margin-bottom: 30px; 
                padding: 20px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; 
                border-radius: 8px; 
            }
            .job-card { 
                border: 1px solid #ddd; 
                margin: 15px 0; 
                padding: 20px; 
                border-radius: 8px; 
                background: #f9f9f9; 
            }
            .job-title { 
                color: #333; 
                font-size: 18px; 
                font-weight: bold; 
                margin-bottom: 10px; 
            }
            .job-company { 
                color: #666; 
                font-size: 16px; 
                margin-bottom: 5px; 
            }
            .job-location { 
                color: #888; 
                font-size: 14px; 
                margin-bottom: 10px; 
            }
            .job-description { 
                color: #555; 
                line-height: 1.6; 
            }
            .nav-links { 
                text-align: center; 
                margin: 20px 0; 
            }
            .nav-links a { 
                margin: 0 15px; 
                padding: 10px 20px; 
                background: #667eea; 
                color: white; 
                text-decoration: none; 
                border-radius: 5px; 
                display: inline-block; 
            }
            .nav-links a:hover { 
                background: #764ba2; 
            }
            .demo-notice { 
                background: #fff3cd; 
                border: 1px solid #ffeaa7; 
                color: #856404; 
                padding: 15px; 
                border-radius: 5px; 
                margin: 20px 0; 
                text-align: center; 
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 Job Portal</h1>
                <p>Find Your Dream Job Today!</p>
            </div>
            
            <div class="demo-notice">
                <strong>📢 Demo Mode:</strong> This is a static demo deployed on Vercel. 
                For full functionality with user registration, login, and job posting, 
                run locally or deploy with a PostgreSQL database.
            </div>
            
            <div class="nav-links">
                <a href="/">🏠 Home</a>
                <a href="/jobs/">💼 Browse Jobs</a>
                <a href="/accounts/register/">👤 Register</a>
                <a href="/accounts/login/">🔐 Login</a>
                <a href="/post-job/">📝 Post Job</a>
            </div>
            
            <h2>📋 Featured Jobs</h2>
            
            <div class="job-card">
                <div class="job-title">Senior Python Developer</div>
                <div class="job-company">🏢 TechCorp Solutions</div>
                <div class="job-location">📍 San Francisco, CA</div>
                <div class="job-description">
                    We are looking for an experienced Python developer to join our growing team. 
                    You'll work on exciting projects using Django, PostgreSQL, and modern web technologies.
                    Requirements: 5+ years Python experience, Django expertise, strong problem-solving skills.
                </div>
            </div>
            
            <div class="job-card">
                <div class="job-title">Frontend React Developer</div>
                <div class="job-company">🏢 StartupX</div>
                <div class="job-location">📍 Remote</div>
                <div class="job-description">
                    Join our dynamic startup as a Frontend Developer! You'll build amazing user interfaces 
                    using React, TypeScript, and modern CSS frameworks. Perfect for someone who loves 
                    creating beautiful, responsive web applications.
                </div>
            </div>
            
            <div class="job-card">
                <div class="job-title">Full Stack Engineer</div>
                <div class="job-company">🏢 Digital Innovations Ltd</div>
                <div class="job-location">📍 New York, NY</div>
                <div class="job-description">
                    We need a versatile Full Stack Engineer to work on both frontend and backend systems. 
                    Experience with Python/Django, JavaScript/React, and cloud platforms required. 
                    Great opportunity for career growth!
                </div>
            </div>
            
            <div class="job-card">
                <div class="job-title">Data Science Manager</div>
                <div class="job-company">🏢 Analytics Pro</div>
                <div class="job-location">📍 Chicago, IL</div>
                <div class="job-description">
                    Lead our data science team in developing machine learning models and analytics solutions. 
                    Looking for someone with 7+ years experience in Python, SQL, machine learning, and team leadership.
                </div>
            </div>
            
            <div class="job-card">
                <div class="job-title">DevOps Engineer</div>
                <div class="job-company">🏢 CloudFirst</div>
                <div class="job-location">📍 Austin, TX</div>
                <div class="job-description">
                    Help us build and maintain scalable cloud infrastructure. Experience with AWS, Docker, 
                    Kubernetes, and CI/CD pipelines essential. Join a team that values automation and efficiency.
                </div>
            </div>
            
            <footer style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; color: #666;">
                <p>💻 <strong>Job Portal Demo</strong> - Built with Django & deployed on Vercel</p>
                <p>🌐 <strong>Live URL:</strong> <a href="https://job-search-five-sage.vercel.app" target="_blank">https://job-search-five-sage.vercel.app</a></p>
                <p>📚 This is a demonstration of a Django job portal application</p>
            </footer>
        </div>
    </body>
    </html>
    """)

@csrf_exempt
def demo_view(request):
    """Generic demo view for all pages"""
    page_name = request.path.strip('/').replace('/', ' - ').title() or 'Home'
    
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Job Portal - {page_name}</title>
        <style>
            body {{ 
                font-family: Arial, sans-serif; 
                margin: 0; 
                padding: 20px; 
                background-color: #f5f5f5; 
            }}
            .container {{ 
                max-width: 800px; 
                margin: 0 auto; 
                background: white; 
                padding: 30px; 
                border-radius: 8px; 
                box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
                text-align: center;
            }}
            .header {{ 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; 
                padding: 20px; 
                border-radius: 8px; 
                margin-bottom: 30px; 
            }}
            .demo-notice {{ 
                background: #fff3cd; 
                border: 1px solid #ffeaa7; 
                color: #856404; 
                padding: 15px; 
                border-radius: 5px; 
                margin: 20px 0; 
            }}
            .nav-links {{ 
                margin: 30px 0; 
            }}
            .nav-links a {{ 
                margin: 0 10px; 
                padding: 10px 20px; 
                background: #667eea; 
                color: white; 
                text-decoration: none; 
                border-radius: 5px; 
                display: inline-block; 
                margin-bottom: 10px;
            }}
            .nav-links a:hover {{ 
                background: #764ba2; 
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 Job Portal - {page_name}</h1>
            </div>
            
            <div class="demo-notice">
                <strong>📢 Demo Mode:</strong> This is a static demo page. 
                In a full deployment, this would be a functional {page_name.lower()} page 
                with user authentication, database integration, and full CRUD operations.
            </div>
            
            <h2>🔧 What this page would normally do:</h2>
            <div style="text-align: left; max-width: 600px; margin: 0 auto;">
                {"".join([
                    "<p><strong>🏠 Home:</strong> Display featured jobs, search functionality, and recent postings</p>",
                    "<p><strong>💼 Jobs:</strong> Browse all available jobs with filtering and pagination</p>",
                    "<p><strong>👤 Register:</strong> User registration with email verification</p>",
                    "<p><strong>🔐 Login:</strong> User authentication and session management</p>",
                    "<p><strong>📝 Post Job:</strong> Employers can post new job listings</p>",
                    "<p><strong>📋 Applications:</strong> Track job applications and status</p>"
                ])}
            </div>
            
            <div class="nav-links">
                <a href="/">🏠 Back to Home</a>
                <a href="/jobs/">💼 Browse Jobs</a>
                <a href="/accounts/register/">👤 Register</a>
                <a href="/accounts/login/">🔐 Login</a>
                <a href="/post-job/">📝 Post Job</a>
            </div>
            
            <footer style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; color: #666;">
                <p>💻 <strong>Job Portal Demo</strong> - Built with Django & deployed on Vercel</p>
                <p>🌐 For full functionality, run locally with SQLite or deploy with PostgreSQL</p>
            </footer>
        </div>
    </body>
    </html>
    """)
