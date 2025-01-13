import os

class Config:
    """Base configuration with default settings."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'Infosys-Springboard-5.0')  # Keep it secret, set via environment variables
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking for performance
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///users.db')  # Use environment variable for DB URI

class DevelopmentConfig(Config):
    """Configuration for development environment."""
    DEBUG = True

