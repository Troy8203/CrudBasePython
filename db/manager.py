# db/manager.py
import oracledb
from config import DB_USER, DB_PASSWORD, DB_DSN
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establish database connection"""
        try:
            self.connection = oracledb.connect(
                user=DB_USER,
                password=DB_PASSWORD,
                dsn=DB_DSN
            )
            self.cursor = self.connection.cursor()
            print("Successfully connected to Oracle Database")
        except oracledb.DatabaseError as e:
            print(f"Database connection error: {e}")
            raise

    def disconnect(self):
        """Close database connection"""
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
                print("Database connection closed")
        except oracledb.DatabaseError as e:
            print(f"Error closing database connection: {e}")
