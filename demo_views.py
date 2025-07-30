from django.http import HttpResponse
from django.template import Template, Context
import os

def demo_view(request):
    """
    Simple demo view for showcasing the job portal
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Job Portal Demo - Django Application</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #333;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 10px;
                padding: 30px;
                margin-bottom: 30px;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            .header h1 {
                color: #2c3e50;
                margin: 0 0 10px 0;
                font-size: 2.5em;
            }
            .subtitle {
                color: #7f8c8d;
                font-size: 1.2em;
            }
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .feature-card {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 10px;
                padding: 25px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease;
            }
            .feature-card:hover {
                transform: translateY(-5px);
            }
            .feature-card h3 {
                color: #2c3e50;
                margin: 0 0 15px 0;
                font-size: 1.3em;
            }
            .feature-list {
                list-style: none;
                padding: 0;
            }
            .feature-list li {
                padding: 5px 0;
                color: #555;
            }
            .feature-list li:before {
                content: "✓ ";
                color: #27ae60;
                font-weight: bold;
            }
            .demo-info {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 10px;
                padding: 25px;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            .tech-stack {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 20px;
            }
            .tech-badge {
                background: #3498db;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9em;
            }
            .status-badge {
                background: #27ae60;
                color: white;
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: bold;
                font-size: 1.1em;
                margin-bottom: 20px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 Job Portal Demo</h1>
                <p class="subtitle">Full-Featured Django Job Search Platform</p>
                <div class="status-badge">✅ Successfully Deployed on Vercel</div>
            </div>

            <div class="features">
                <div class="feature-card">
                    <h3>👥 User Management</h3>
                    <ul class="feature-list">
                        <li>Job Seeker Registration</li>
                        <li>Employer Registration</li>
                        <li>Profile Management</li>
                        <li>Authentication System</li>
                        <li>Role-based Access</li>
                    </ul>
                </div>

                <div class="feature-card">
                    <h3>💼 Job Management</h3>
                    <ul class="feature-list">
                        <li>Post Job Listings</li>
                        <li>Job Search & Filtering</li>
                        <li>Category Management</li>
                        <li>Job Application System</li>
                        <li>Application Tracking</li>
                    </ul>
                </div>

                <div class="feature-card">
                    <h3>🎯 Advanced Features</h3>
                    <ul class="feature-list">
                        <li>Responsive Design</li>
                        <li>Admin Panel</li>
                        <li>File Upload (Resume/CV)</li>
                        <li>Email Notifications</li>
                        <li>Search Functionality</li>
                    </ul>
                </div>
            </div>

            <div class="demo-info">
                <h3>🎉 Demo Status</h3>
                <p>This Django job portal application has been successfully deployed to Vercel as a public demo.</p>
                <p>The application includes all the core features of a modern job search platform built with Django.</p>
                
                <h4>🛠️ Technology Stack</h4>
                <div class="tech-stack">
                    <span class="tech-badge">Django 5.2.4</span>
                    <span class="tech-badge">Python</span>
                    <span class="tech-badge">SQLite</span>
                    <span class="tech-badge">HTML/CSS</span>
                    <span class="tech-badge">Bootstrap</span>
                    <span class="tech-badge">Vercel</span>
                </div>

                <h4>📊 Application Components</h4>
                <p><strong>Apps:</strong> accounts (user management), jobs (job listings), admin panel</p>
                <p><strong>Models:</strong> User profiles, Job listings, Applications, Categories</p>
                <p><strong>Views:</strong> Authentication, Job CRUD, Search, Apply functionality</p>
                
                <h4>🔗 GitHub Repository</h4>
                <p>Full source code available with detailed documentation and screenshots</p>
                
                <p style="margin-top: 30px; color: #7f8c8d;">
                    <strong>Note:</strong> This is a demonstration deployment showcasing the application structure and features.
                    The full application with database functionality runs locally and includes user authentication,
                    job posting, application management, and admin features.
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html_content)
