# main.py
from models.employee import EmployeeModel

def main():
    employee_model = EmployeeModel()
    
    # Conectar y crear tabla
    #employee_model.create_table()
    
    # Crear un empleado
    employee_model.insert_employee(3, "John Doe", "john@example.com", 50000)
    
    # Resto de operaciones CRUD
    employee_model.get_all_employees()
    employee_model.get_employee_by_id(1)
    employee_model.update_employee(1, name="John Updated", salary=55000)
    employee_model.delete_employee(2)

    

if __name__ == "__main__":
    main()
