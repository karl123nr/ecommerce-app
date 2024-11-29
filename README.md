# E-commerce Application

A simple e-commerce application built with React, FastAPI, and PostgreSQL, containerized with Docker.

## Features

- User authentication (login/register)
- Product catalog
- Shopping cart
- Order management
- Cash-only payments (no payment integration)

## Tech Stack

- Frontend: React with Material-UI
- Backend: FastAPI
- Database: PostgreSQL
- Containerization: Docker

## Getting Started

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone this repository:
```bash
git clone <repository-url>
cd ecommerce-app
```

3. Start the application:
```bash
docker-compose up --build
```

4. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Environment Variables

The application uses the following environment variables:

### Backend
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT secret key (change in production)

### Frontend
- `REACT_APP_API_URL`: Backend API URL

## Project Structure

```
ecommerce-app/
├── frontend/           # React frontend
├── backend/           # FastAPI backend
│   └── app/
│       ├── main.py    # Main application
│       ├── models.py  # Database models
│       ├── schemas.py # Pydantic schemas
│       └── crud.py    # Database operations
└── docker-compose.yml # Docker composition
```
