# Cloud Deployment Guide

## Option 1: Render.com (Free)

1. Create a GitHub account and push your code
2. Go to [render.com](https://render.com) and sign up
3. Click "New Web Service"
4. Connect your GitHub repository
5. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
6. Click "Create Web Service"

## Option 2: Railway ($5/month)

1. Go to [railway.app](https://railway.app) 
2. Create new project > Deploy from GitHub repo
3. Add SQLite database
4. Deploy

## Option 3: PythonAnywhere (Free)

1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create account
3. Go to "Web" > "Add a new web app"
4. Choose "Flask" and Python version
5. Upload your files via Files tab
6. Configure WSGI file to point to app.py
7. Click "Reload"

## Option 4: Replit (Free)

1. Go to [replit.com](https://replit.com)
2. Create new Repl > Flask
3. Upload your files
4. Click "Run"

## Required Changes for Deployment

1. Update app.py to use environment variables:
```
python
import os
port = int(os.environ.get('PORT', 10000))
app.run(host="0.0.0.0", port=port)
```

2. For deployment, you'll need to:
   - Use a production database (PostgreSQL/MySQL) instead of SQLite
   - Set secret_key securely
   - Enable HTTPS

## Accessing Your Deployed App

After deployment, you'll get a URL like:
`https://your-app-name.onrender.com`

Share this URL with others to access the system.
