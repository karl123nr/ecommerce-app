# Deploying to Render.com

## Step 1: Prepare Your Application

1. Create a `render.yaml` file in your project root:
```yaml
services:
  - type: web
    name: ecommerce-frontend
    env: static
    buildCommand: cd frontend && npm install && npm run build
    staticPublishPath: ./frontend/build
    envVars:
      - key: REACT_APP_API_URL
        fromService:
          type: web
          name: ecommerce-backend
          envVarKey: RENDER_EXTERNAL_URL

  - type: web
    name: ecommerce-backend
    env: python
    buildCommand: cd backend && pip install -r requirements.txt
    startCommand: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: ecommerce-db
          property: connectionString

databases:
  - name: ecommerce-db
    databaseName: ecommerce
    user: ecommerce
```

2. Update your frontend's package.json to include a build script:
```json
{
  "scripts": {
    "build": "react-scripts build"
  }
}
```

## Step 2: Deploy to Render

1. Go to [render.com](https://render.com) and create an account

2. Click "New +" and select "Blueprint" from the dropdown

3. Connect your GitHub/GitLab repository or upload your code directly:
   - If using direct upload:
     1. Zip your project files
     2. Click "Upload Files"
     3. Select your zip file

4. Your services will be automatically configured based on render.yaml

5. Click "Apply" and wait for deployment to complete

## Step 3: Access Your Application

- Frontend URL: https://ecommerce-frontend-xxxx.onrender.com
- Backend URL: https://ecommerce-backend-xxxx.onrender.com
- Database is automatically configured

## Environment Variables
All environment variables are automatically managed by Render based on the render.yaml configuration.

## Maintenance

### Update Your Application
1. Go to your service dashboard on Render
2. Click "Manual Deploy"
3. Select "Deploy latest commit" or upload new files

### View Logs
1. Go to your service dashboard
2. Click "Logs" in the left sidebar

### Monitor Usage
1. Go to your service dashboard
2. View metrics under "Monitoring"

## Advantages of Using Render
1. No Docker knowledge required
2. Free SSL certificates
3. Automatic CI/CD
4. Built-in database management
5. Zero-configuration deployments
6. Free tier available
7. Excellent documentation and support
