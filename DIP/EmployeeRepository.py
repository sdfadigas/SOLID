from abc import ABC
from abc import abstractmethod

class EmployeeRepository(ABC):
    @abstractmethod
    def get_employee_data(self, employee_id):
        pass

class EmployeeDataAccess(EmployeeRepository):
    def get_employee_data(self, employee_id):
        # code to retrieve employee data from database
        pass

class EmployeePrinter:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository
        
    def print_employee_data(self, employee_id):
        employee_data = self.employee_repository.get_employee_data(employee_id)
        print("Name:", employee_data['name'])
        print("ID number:", employee_data['id_number'])
        print("Salary:", employee_data['salary'])

class ContractorPrinter:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository
        
    def print_contractor_data(self, contractor_id):
        contractor_data = self.employee_repository.get_employee_data(contractor_id)
        print("Name:", contractor_data['name'])
        print("ID number:", contractor_data['id_number'])
        print("Pay:", contractor_data['hourly_rate'] * 40)
