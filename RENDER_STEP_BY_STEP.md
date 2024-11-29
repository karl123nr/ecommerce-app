# Step-by-Step Render Deployment Guide

## Step 1: Prepare Your Application Files

1. First, we need to create a production build of your React frontend. In your local terminal:
```bash
cd frontend
npm run build
```

2. Create a new file `frontend/static.json` for static site settings:
```json
{
  "root": "build/",
  "routes": {
    "/**": "index.html"
  },
  "headers": {
    "/**": {
      "Cache-Control": "public, max-age=0, must-revalidate"
    }
  }
}
```

## Step 2: Sign Up for Render

1. Go to https://render.com
2. Click "Sign Up"
3. You can sign up with GitHub or email

## Step 3: Deploy the PostgreSQL Database

1. From your Render dashboard, click "New +"
2. Select "PostgreSQL"
3. Fill in the details:
   - Name: `ecommerce-db`
   - Database: `ecommerce`
   - User: `ecommerce_user`
   - Region: Choose closest to your users
4. Click "Create Database"
5. **Important**: Save the "Internal Database URL" shown - you'll need this later

## Step 4: Deploy the Backend

1. From your dashboard, click "New +"
2. Select "Web Service"
3. Choose "Upload Files" if not using Git
4. Fill in the details:
   - Name: `ecommerce-backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Under "Environment Variables", add:
   - `DATABASE_URL`: (paste the Internal Database URL from Step 3)
   - `SECRET_KEY`: (generate a random string or use a secure key)
6. Click "Create Web Service"

## Step 5: Deploy the Frontend

1. From dashboard, click "New +"
2. Select "Static Site"
3. Upload your frontend files
4. Fill in the details:
   - Name: `ecommerce-frontend`
   - Build Command: `npm install && npm run build`
   - Publish Directory: `build`
5. Under "Environment Variables", add:
   - `REACT_APP_API_URL`: (your backend URL from Step 4)
6. Click "Create Static Site"

## Step 6: Connect Frontend to Backend

1. Go to your frontend service settings
2. Add CORS headers in Environment Variables:
```
RENDER_HEADERS={"Access-Control-Allow-Origin": "*"}
```

## Step 7: Verify Deployment

1. Test backend API:
   - Go to `https://your-backend-url/docs`
   - You should see the FastAPI documentation

2. Test frontend:
   - Go to `https://your-frontend-url`
   - Try registering a new user
   - Try logging in
   - Browse products

## Common Issues and Solutions

### Backend Won't Start
1. Check logs in Render dashboard
2. Common fixes:
   - Verify DATABASE_URL is correct
   - Check if all requirements are installed
   - Make sure start command is correct

### Frontend Can't Connect to Backend
1. Verify REACT_APP_API_URL is correct
2. Check CORS settings
3. Make sure backend is running

### Database Connection Issues
1. Check DATABASE_URL format
2. Verify database is active
3. Check database credentials

## Monitoring Your Application

### View Logs
1. Go to service dashboard
2. Click "Logs"
3. You can filter by:
   - Build logs
   - Runtime logs
   - System logs

### Monitor Performance
1. Go to service dashboard
2. Click "Metrics"
3. You can view:
   - CPU usage
   - Memory usage
   - Response times
   - Request counts

### Set Up Alerts
1. Go to service settings
2. Click "Alerts"
3. You can set alerts for:
   - Service down
   - High CPU usage
   - High memory usage

## Updating Your Application

### To Update Frontend
1. Make changes locally
2. Test locally
3. Upload new files to Render
4. Render will automatically rebuild and deploy

### To Update Backend
1. Make changes locally
2. Test locally
3. Upload new files to Render
4. Service will automatically rebuild and deploy

## Cost Management
- Start with free tier
- Monitor usage in dashboard
- Set up billing alerts
- Scale resources as needed

## Security Best Practices
1. Never commit sensitive data
2. Use environment variables for:
   - API keys
   - Database credentials
   - Secret keys
3. Enable automatic HTTPS
4. Regularly update dependencies

## Backup and Recovery
1. Database backups:
   - Automatic daily backups
   - Manual backup option
   - 7-day retention on free tier
2. Code backups:
   - Keep local copies
   - Use version control
   - Download from Render if needed
