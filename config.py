# config.py
import os

class Config:
    SECRET_KEY = 'quest-university-secret-key-2024'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'dreamteam'  # Add your MySQL password
    MYSQL_DB = 'quest_result_system'
    MYSQL_CURSORCLASS = 'DictCursor'