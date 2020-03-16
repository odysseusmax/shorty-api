import os

class Config:
    DATABASE_URI = os.environ.get('DATABASE_URI', None) or ""
