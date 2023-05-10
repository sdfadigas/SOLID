class Employee:
    def __init__(self, name, id_number, salary):
        self.name = name
        self.id_number = id_number
        self.salary = salary
        
    def get_name(self):
        return self.name
    
    def get_id_number(self):
        return self.id_number
    
    def get_salary(self):
        return self.salary
    
class EmployeePrinter:
    def __init__(self, employee):
        self.employee = employee
        
    def print_employee_data(self):
        print("Name:", self.employee.get_name())
        print("ID number:", self.employee.get_id_number())
        print("Salary:", self.employee.get_salary())
