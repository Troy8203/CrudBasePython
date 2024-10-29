import getpass
import oracledb
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establish database connection"""
        try:
            password = getpass.getpass("Enter password for the database user: ")
            self.connection = oracledb.connect(
                user="db272",
                password=password,
                dsn="localhost:1521/XEPDB1"
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

    def create_table(self):
        """Create a sample employees table"""
        try:
            self.cursor.execute("""
                CREATE TABLE employees (
                    emp_id NUMBER PRIMARY KEY,
                    name VARCHAR2(100),
                    email VARCHAR2(100) UNIQUE,
                    hire_date DATE,
                    salary NUMBER(10,2)
                )
            """)
            self.connection.commit()
            print("Table 'employees' created successfully")
        except oracledb.DatabaseError as e:
            print(f"Error creating table: {e}")
            self.connection.rollback()

    def insert_employee(self, emp_id, name, email, salary):
        """Create - Insert a new employee record"""
        try:
            self.cursor.execute("""
                INSERT INTO employees (emp_id, name, email, hire_date, salary)
                VALUES (:1, :2, :3, :4, :5)
            """, (emp_id, name, email, datetime.now(), salary))
            self.connection.commit()
            print(f"Employee {name} inserted successfully")
        except oracledb.DatabaseError as e:
            print(f"Error inserting employee: {e}")
            self.connection.rollback()

    def get_all_employees(self):
        """Read - Fetch all employees"""
        try:
            self.cursor.execute("SELECT * FROM employees")
            employees = self.cursor.fetchall()
            if not employees:
                print("No employees found")
                return []
            
            # Print employees in a formatted way
            print("\nEmployee List:")
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}, Email: {emp[2]}, Hire Date: {emp[3]}, Salary: {emp[4]}")
            return employees
        except oracledb.DatabaseError as e:
            print(f"Error fetching employees: {e}")
            return []

    def get_employee_by_id(self, emp_id):
        """Read - Fetch a specific employee by ID"""
        try:
            self.cursor.execute("SELECT * FROM employees WHERE emp_id = :1", (emp_id,))
            employee = self.cursor.fetchone()
            if employee:
                print(f"\nEmployee found:")
                print(f"ID: {employee[0]}, Name: {employee[1]}, Email: {employee[2]}, "
                      f"Hire Date: {employee[3]}, Salary: {employee[4]}")
                return employee
            print(f"No employee found with ID {emp_id}")
            return None
        except oracledb.DatabaseError as e:
            print(f"Error fetching employee: {e}")
            return None

    def update_employee(self, emp_id, name=None, email=None, salary=None):
        """Update - Modify an existing employee's information"""
        try:
            # Build dynamic update query based on provided parameters
            update_parts = []
            params = []
            if name:
                update_parts.append("name = :1")
                params.append(name)
            if email:
                update_parts.append("email = :2")
                params.append(email)
            if salary:
                update_parts.append("salary = :3")
                params.append(salary)
            
            if not update_parts:
                print("No updates provided")
                return False

            query = f"UPDATE employees SET {', '.join(update_parts)} WHERE emp_id = :id"
            params.append(emp_id)
            
            self.cursor.execute(query, params)
            if self.cursor.rowcount > 0:
                self.connection.commit()
                print(f"Employee {emp_id} updated successfully")
                return True
            else:
                print(f"No employee found with ID {emp_id}")
                return False
        except oracledb.DatabaseError as e:
            print(f"Error updating employee: {e}")
            self.connection.rollback()
            return False

    def delete_employee(self, emp_id):
        """Delete - Remove an employee record"""
        try:
            self.cursor.execute("DELETE FROM employees WHERE emp_id = :1", (emp_id,))
            if self.cursor.rowcount > 0:
                self.connection.commit()
                print(f"Employee {emp_id} deleted successfully")
                return True
            else:
                print(f"No employee found with ID {emp_id}")
                return False
        except oracledb.DatabaseError as e:
            print(f"Error deleting employee: {e}")
            self.connection.rollback()
            return False

def main():
    """Example usage of the DatabaseManager class"""
    db = DatabaseManager()
    try:
        # Connect to database
        db.connect()

        # Create table (uncomment if needed)
        db.create_table()

        # Create - Insert employees
        db.insert_employee(1, "John Doe", "john@example.com", 50000)
        db.insert_employee(2, "Jane Smith", "jane@example.com", 60000)

        # Read - Get all employees
        print("\nFetching all employees:")
        db.get_all_employees()

        # Read - Get specific employee
        print("\nFetching specific employee:")
        db.get_employee_by_id(1)

        # Update - Modify employee
        print("\nUpdating employee:")
        db.update_employee(1, name="John Updated", salary=55000)

        # Read - Verify update
        print("\nVerifying update:")
        db.get_employee_by_id(1)

        # Delete - Remove employee
        print("\nDeleting employee:")
        db.delete_employee(2)

        # Read - Verify deletion
        print("\nFinal employee list:")
        db.get_all_employees()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Always close the connection
        db.disconnect()

if __name__ == "__main__":
    main()
