# models/employee.py
import oracledb
from db.manager import DatabaseManager
from datetime import datetime

class EmployeeModel:
    def __init__(self):
        # Crea una instancia de la conexión
        self.db_manager = DatabaseManager()

    def create_table(self):
        """Crear la tabla de empleados si no existe"""
        self.db_manager.connect()  # Abre la conexión
        try:
            self.db_manager.cursor.execute("""
                CREATE TABLE employees (
                    emp_id NUMBER PRIMARY KEY,
                    name VARCHAR2(100),
                    email VARCHAR2(100) UNIQUE,
                    hire_date DATE,
                    salary NUMBER(10,2)
                )
            """)
            self.db_manager.connection.commit()
            print("Tabla 'employees' creada con éxito")
        except oracledb.DatabaseError as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            self.db_manager.disconnect()  # Cierra la conexión

    def insert_employee(self, emp_id, name, email, salary):
        """Insertar un nuevo empleado"""
        self.db_manager.connect()
        try:
            self.db_manager.cursor.execute("""
                INSERT INTO employees (emp_id, name, email, hire_date, salary)
                VALUES (:1, :2, :3, :4, :5)
            """, (emp_id, name, email, datetime.now(), salary))
            self.db_manager.connection.commit()
            print(f"Empleado {name} insertado con éxito")
        except oracledb.DatabaseError as e:
            print(f"Error al insertar empleado: {e}")
        finally:
            self.db_manager.disconnect()

    def get_all_employees(self):
        """Obtener todos los empleados"""
        self.db_manager.connect()
        try:
            self.db_manager.cursor.execute("SELECT * FROM employees")
            employees = self.db_manager.cursor.fetchall()
            if not employees:
                print("No hay empleados")
                return []
            
            print("\nLista de Empleados:")
            for emp in employees:
                print(f"ID: {emp[0]}, Nombre: {emp[1]}, Email: {emp[2]}, Fecha de Contratación: {emp[3]}, Salario: {emp[4]}")
            return employees
        except oracledb.DatabaseError as e:
            print(f"Error al obtener empleados: {e}")
            return []
        finally:
            self.db_manager.disconnect()

    def get_employee_by_id(self, emp_id):
        """Obtener un empleado por su ID"""
        self.db_manager.connect()
        try:
            self.db_manager.cursor.execute("SELECT * FROM employees WHERE emp_id = :1", (emp_id,))
            employee = self.db_manager.cursor.fetchone()
            if employee:
                print(f"Empleado encontrado: ID: {employee[0]}, Nombre: {employee[1]}, Email: {employee[2]}, "
                      f"Fecha de Contratación: {employee[3]}, Salario: {employee[4]}")
                return employee
            print(f"No se encontró ningún empleado con ID {emp_id}")
            return None
        except oracledb.DatabaseError as e:
            print(f"Error al obtener empleado: {e}")
            return None
        finally:
            self.db_manager.disconnect()

    def update_employee(self, emp_id, name=None, email=None, salary=None):
        """Actualizar información de un empleado"""
        self.db_manager.connect()
        try:
            # Crear consulta de actualización solo con campos necesarios
            if name:
                self.db_manager.cursor.execute("UPDATE employees SET name = :1 WHERE emp_id = :2", (name, emp_id))
            if email:
                self.db_manager.cursor.execute("UPDATE employees SET email = :1 WHERE emp_id = :2", (email, emp_id))
            if salary:
                self.db_manager.cursor.execute("UPDATE employees SET salary = :1 WHERE emp_id = :2", (salary, emp_id))
            self.db_manager.connection.commit()
            print(f"Empleado {emp_id} actualizado con éxito")
        except oracledb.DatabaseError as e:
            print(f"Error al actualizar empleado: {e}")
        finally:
            self.db_manager.disconnect()

    def delete_employee(self, emp_id):
        """Eliminar un empleado"""
        self.db_manager.connect()
        try:
            self.db_manager.cursor.execute("DELETE FROM employees WHERE emp_id = :1", (emp_id,))
            self.db_manager.connection.commit()
            print(f"Empleado {emp_id} eliminado con éxito")
        except oracledb.DatabaseError as e:
            print(f"Error al eliminar empleado: {e}")
        finally:
            self.db_manager.disconnect()
