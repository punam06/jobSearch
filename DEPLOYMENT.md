# 🚀 Job Portal - Deployment Guide

## Deploy to Vercel (Recommended)

### Prerequisites
- Git repository (already set up)
- Vercel account (free at vercel.com)
- GitHub account

### Step-by-Step Deployment

#### 1. Push to GitHub (if not already done)
```bash
# If you haven't already, push to GitHub
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

#### 2. Deploy to Vercel

**Option A: Using Vercel Dashboard (Easiest)**
1. Go to [vercel.com](https://vercel.com) and sign up/login
2. Click "New Project"
3. Connect your GitHub account
4. Select your job portal repository
5. Configure the project:
   - Framework Preset: `Other`
   - Root Directory: `./` (leave empty)
   - Build Command: `chmod +x build_files.sh && ./build_files.sh`
   - Output Directory: `staticfiles_build`
   - Install Command: `pip install -r requirements.txt`
6. Add Environment Variables (if needed):
   - `DJANGO_SETTINGS_MODULE=jobportal.settings`
7. Click "Deploy"

**Option B: Using Vercel CLI**
```bash
# Install Vercel CLI (if not already installed)
npm install -g vercel

# Login to Vercel
vercel login

# Deploy from project root
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? Select your scope
# - Link to existing project? No
# - Project name: job-portal (or your preferred name)
# - Directory: ./
# - Auto-detected settings okay? Yes

# For production deployment
vercel --prod
```

#### 3. Configure Domain (Optional)
- In Vercel dashboard, go to your project
- Click "Domains" tab
- Add your custom domain or use the provided .vercel.app domain

### 🔧 Important Configuration Notes

#### Database Considerations
- The app currently uses SQLite, which works for demo purposes
- For production, consider upgrading to PostgreSQL:
  1. Add PostgreSQL dependency to requirements.txt
  2. Update DATABASES setting in settings.py
  3. Add database environment variables in Vercel

#### File Uploads
- Media files (resume uploads) are stored locally
- For production, consider cloud storage (AWS S3, Cloudinary)
- Update MEDIA_ROOT and MEDIA_URL settings accordingly

#### Environment Variables
Add these in Vercel dashboard under Settings > Environment Variables:
- `DJANGO_SECRET_KEY`: Generate a new secret key for production
- `DEBUG`: Set to `False` for production
- Database credentials (if using external database)

### 🎯 Post-Deployment Steps

#### 1. Create Superuser (First time only)
After successful deployment, you need to create a superuser account:

**Option A: Using Vercel Functions (if supported)**
```bash
# This might not work on all Vercel deployments
vercel env pull
python manage.py createsuperuser
```

**Option B: Create through Django shell in production**
Since Vercel is serverless, you'll need to:
1. Use the provided admin account (admin/admin123) from sample data
2. Or set up a different approach for user management

#### 2. Load Sample Data
The deployment automatically includes sample data from the management command.

#### 3. Test the Application
- Visit your Vercel URL
- Test all features:
  - User registration
  - Job posting (as employer)
  - Job application (as applicant)
  - Search functionality
  - Admin panel

### 🔍 Troubleshooting

#### Common Issues and Solutions

**1. Static Files Not Loading**
```bash
# Ensure build script ran successfully
# Check vercel.json configuration
# Verify STATIC_ROOT setting
```

**2. Database Issues**
```bash
# For SQLite on Vercel, the database is ephemeral
# Consider using external database for persistence
```

**3. Media Files Not Accessible**
```bash
# Vercel has limitations with file uploads
# Consider cloud storage integration
```

**4. Build Failures**
```bash
# Check build logs in Vercel dashboard
# Ensure all dependencies in requirements.txt
# Verify Python version compatibility
```

### 📊 Monitoring and Analytics

#### Vercel Analytics
- Enable in Vercel dashboard for traffic insights
- Monitor performance and usage

#### Application Monitoring
- Check Django logs through Vercel function logs
- Monitor database performance
- Set up error tracking (Sentry integration)

### 🔒 Security Considerations

#### Production Settings
Update `settings.py` for production:
```python
# Security settings
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

#### Environment Variables
Never commit sensitive data:
- Secret keys
- Database credentials
- API keys
- Use Vercel's environment variables

### 🚀 Alternative Deployment Options

#### Netlify (Limited Django Support)
- Netlify is primarily for static sites
- Django requires server-side processing
- Not recommended for this application

#### Railway
```bash
# Install Railway CLI
pip install railway-cli

# Deploy to Railway
railway login
railway init
railway up
```

#### Heroku
```bash
# Install Heroku CLI
# Create Procfile
echo "web: gunicorn jobportal.wsgi" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

#### DigitalOcean App Platform
- Create account on DigitalOcean
- Use App Platform for Django deployment
- Configure database and environment variables

### 📈 Scaling Considerations

#### Database Scaling
- Migrate to PostgreSQL for better performance
- Consider database connection pooling
- Implement database backup strategies

#### Media File Storage
- Integrate AWS S3 or similar cloud storage
- Configure CDN for faster file delivery
- Implement proper file upload validation

#### Performance Optimization
- Enable Django caching
- Optimize database queries
- Implement search indexing for job search

### 🎉 Success Indicators

Your deployment is successful when:
- ✅ Homepage loads with job listings
- ✅ User registration/login works
- ✅ Employers can post jobs
- ✅ Applicants can apply with file uploads
- ✅ Search functionality works
- ✅ Admin panel is accessible
- ✅ All static files load correctly

### 📞 Support and Resources

- **Vercel Documentation**: https://vercel.com/docs
- **Django Deployment Guide**: https://docs.djangoproject.com/en/stable/howto/deployment/
- **Project Repository**: Your GitHub repository
- **Issues**: Create issues in your GitHub repository

---

🎯 **Your Job Portal is now live and ready for users!** 

Share your Vercel URL to showcase your Django development skills.
