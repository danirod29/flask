import os

class Config:
    SQLALCHEMY_DATABASE_URL=os.environ.get("DATABASE_URL")