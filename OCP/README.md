The **Open-Closed Principle (OCP)** is another SOLID principle in object-oriented programming. It states that classes should be open for extension but closed for modification, meaning that we should be able to add new functionality to a class without modifying its existing code.

To demonstrate how the OCP works in the employee data management system, let's say we now need to add a new feature to display the employee's start date along with their name, ID number, and salary.

To follow the OCP, I did not modify the existing `EmployeePrinter` class. Instead, we should create a new class that extends the functionality of the `EmployeePrinter` class.

In the `EmployeeStartDatePrinter` class, I have extended the functionality of the `EmployeePrinter` class by adding a `start_date` attribute to the constructor and a `print_employee_data` method that prints out the employee's start date.

I have also used inheritance to reuse the code from the `EmployeePrinter` class, which is already responsible for displaying the employee's name, ID number, and salary.

By extending the EmployeePrinter class rather than modifying it, we are following the OCP. If I needed to add more features to the employee data management system in the future, I could create new classes that extend existing classes without modifying their existing code.

This principle promotes the reuse of existing code and makes our system more flexible and scalable, as we can add new functionality without breaking the existing code