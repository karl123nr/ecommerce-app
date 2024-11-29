# Deploying to Vultr

## Prerequisites
1. A Vultr account (Sign up at https://www.vultr.com if you haven't)
2. Your application code in a Git repository
3. A domain name (optional, but recommended for HTTPS)

## Step 1: Create a Vultr Instance
1. Log in to your Vultr account
2. Click "Deploy Server"
3. Choose server location (pick the one closest to your target users)
4. Select "Docker" from the Server Type options
5. Choose a server size (Recommended: at least 2GB RAM, 1 CPU)
   - For this app, select the $10/month plan (2GB RAM, 1 CPU) or higher
6. Add your SSH key (or create a new one)
7. Click "Deploy Now"

## Step 2: Initial Server Setup
1. Get your server's IP address from Vultr dashboard
2. SSH into your server:
```bash
ssh root@YOUR_SERVER_IP
```

3. Update the system:
```bash
apt update && apt upgrade -y
```

4. Install Docker Compose (Docker is pre-installed):
```bash
curl -L "https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

## Step 3: Configure Domain (Optional but Recommended)
1. Add DNS A record pointing to your Vultr server IP
2. Install Certbot for SSL:
```bash
apt install certbot python3-certbot-nginx -y
```

3. Get SSL certificate:
```bash
certbot --nginx -d yourdomain.com
```

## Step 4: Deploy Application
### Option 1: Clone Repository
1. Clone your repository:
```bash
git clone YOUR_REPO_URL
cd ecommerce-app
```

2. Create environment file:
```bash
cat > .env << EOL
DATABASE_URL=postgresql://postgres:postgres@db:5432/ecommerce
SECRET_KEY=your-secure-secret-key
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=ecommerce
EOL
```

3. Modify docker-compose.yml for production:
```bash
# Add these lines under the frontend service
    environment:
      - REACT_APP_API_URL=https://yourdomain.com  # or http://your_server_ip
```

4. Start the application:
```bash
docker-compose up -d
```

### Option 2: Upload Files Directly
1. Create a deployment directory on your Vultr server:
```bash
mkdir -p /opt/ecommerce-app
```

2. From your local machine, use SCP to upload the files (run these commands in your local terminal):
```bash
# For Windows PowerShell/Command Prompt:
scp -r frontend backend docker-compose.yml root@YOUR_SERVER_IP:/opt/ecommerce-app/

# Alternative: If you're using WinSCP:
# 1. Download WinSCP from https://winscp.net
# 2. Connect to your server using:
#    - Host: YOUR_SERVER_IP
#    - Username: root
#    - Your SSH private key or password
# 3. Drag and drop the files to /opt/ecommerce-app/
```

3. SSH into your server and navigate to the app directory:
```bash
ssh root@YOUR_SERVER_IP
cd /opt/ecommerce-app
```

## Step 5: Configure Nginx Reverse Proxy
1. Install Nginx:
```bash
apt install nginx -y
```

2. Create Nginx configuration:
```bash
cat > /etc/nginx/sites-available/ecommerce << EOL
server {
    listen 80;
    server_name yourdomain.com;  # or your server IP

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host \$host;
        proxy_cache_bypass \$http_upgrade;
    }

    location /api {
        rewrite ^/api/(.*) /\$1 break;
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host \$host;
        proxy_cache_bypass \$http_upgrade;
    }
}
EOL
```

3. Enable the site:
```bash
ln -s /etc/nginx/sites-available/ecommerce /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

## Step 6: Configure Firewall
```bash
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw enable
```

## Maintenance and Monitoring

### View logs:
```bash
# All containers
docker-compose logs

# Specific service
docker-compose logs frontend
docker-compose logs backend
docker-compose logs db
```

### Update application:
```bash
# Pull latest code
git pull

# Rebuild and restart containers
docker-compose down
docker-compose up -d --build
```

### Backup database:
```bash
# Create backup
docker-compose exec db pg_dump -U postgres ecommerce > backup.sql

# Restore backup
cat backup.sql | docker-compose exec -T db psql -U postgres ecommerce
```

## Security Recommendations
1. Change default database passwords in .env file
2. Use a strong SECRET_KEY for JWT authentication
3. Enable HTTPS using Let's Encrypt
4. Regularly update system packages and Docker images
5. Set up automated backups
6. Monitor server resources using Vultr dashboard

## Troubleshooting
1. Check container status:
```bash
docker-compose ps
```

2. View container logs:
```bash
docker-compose logs -f
```

3. Restart services:
```bash
docker-compose restart
```

4. Check Nginx error logs:
```bash
tail -f /var/log/nginx/error.log
```
