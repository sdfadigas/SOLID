from abc import ABC
from abc import abstractmethod

class Employee(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_id_number(self):
        pass
    
    @abstractmethod
    def get_salary(self):
        pass

class Contractor(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_id_number(self):
        pass
    
    @abstractmethod
    def calculate_pay(self, hours_worked):
        pass

class EmployeePrinter:
    def __init__(self, employee):
        self.employee = employee
        
    def print_employee_data(self):
        print("Name:", self.employee.get_name())
        print("ID number:", self.employee.get_id_number())
        print("Salary:", self.employee.get_salary())

class ContractorPrinter:
    def __init__(self, contractor):
        self.contractor = contractor
        
    def print_contractor_data(self):
        print("Name:", self.contractor.get_name())
        print("ID number:", self.contractor.get_id_number())
        print("Pay:", self.contractor.calculate_pay(40))
