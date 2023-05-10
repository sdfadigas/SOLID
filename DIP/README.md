The **Dependency Inversion Principle (DIP)** is another SOLID principle in object-oriented programming. It states that high-level modules should not depend on low-level modules, both should depend on abstractions. Abstractions should not depend on details, but details should depend on abstractions.

In our employee data management system, let's say we have a `EmployeeDataAccess` class that retrieves employee data from a database. The `EmployeePrinter` and `ContractorPrinter` classes depend on the `EmployeeDataAccess` class to retrieve the employee and contractor data.

However, by following the DIP, we should invert the dependency between the `EmployeePrinter` and `ContractorPrinter` classes and the `EmployeeDataAccess` class. Instead of the high-level modules (i.e., `EmployeePrinter` and `ContractorPrinter`) depending on the low-level module (i.e., `EmployeeDataAccess`), we should create an abstraction that both the high-level and low-level modules can depend on.

So we create an `EmployeeRepository` interface that defines the methods needed to retrieve employee data.

Modifying the `EmployeeDataAccess` class to implement the `EmployeeRepository` interface. And modifying the `EmployeePrinter` and `ContractorPrinter` classes to use the `EmployeeRepository` interface instead of the `EmployeeDataAccess` class.

In the modified `EmployeePrinter` and `ContractorPrinter` classes, we are now using the `EmployeeRepository` interface to retrieve the employee and contractor data, rather than the `EmployeeDataAccess` class directly. This way, the high-level modules (i.e., `EmployeePrinter` and `ContractorPrinter`) depend on the abstraction (i.e., the `EmployeeRepository` interface) rather than the details of the implementation (i.e., the `EmployeeDataAccess` class).

This inversion of dependency allows for greater flexibility and easier maintenance of the system. The high-level modules no longer depend on the low-level details of the `EmployeeDataAccess` class, which means we can easily swap out the implementation of the `EmployeeRepository` interface in the future without affecting the high-level modules. This promotes the development of more modular and extensible systems.