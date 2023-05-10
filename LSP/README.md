The **Liskov Substitution Principle (LSP)** is another SOLID principle in object-oriented programming. It states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

To demonstrate how the LSP works in our employee data management system, I created a new type of employee called a "manager". A manager has all the attributes of a regular employee, plus an additional attribute for their department.

To follow the LSP, we should be able to use a `Manager` object anywhere we would use an Employee object, without affecting the correctness of the program. Creating a `Manager` class that inherits from the `Employee` class.

In the `Manager` class, I have inherited the Employee class and added a department attribute to the constructor and a `get_department` method to retrieve the department attribute.

Modifying the `EmployeePrinter` class to print out the department attribute for managers.

In the modified `EmployeePrinter` class, I have added an if statement to check if the employee is a manager. If so, I print out the department attribute using the `get_department` method.

By checking the type of the employee object using the isinstance function, we are following the LSP. We can use a `Manager` object anywhere we would use an `Employee` object, and the `EmployeePrinter` class can handle both types of objects without affecting the correctness of the program.

This principle promotes code reuse and encourages the creation of flexible, scalable systems that can handle new types of objects without breaking existing code.