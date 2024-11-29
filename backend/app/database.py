from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Get the Database URL from environment variable
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Handle special case for Render.com Postgres connection
if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Fallback to local database if no URL is provided
if not SQLALCHEMY_DATABASE_URL:
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/ecommerce"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
