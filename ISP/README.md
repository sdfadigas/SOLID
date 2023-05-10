The **Interface Segregation Principle (ISP)** is another SOLID principle in object-oriented programming. It states that clients should not be forced to depend on interfaces they do not use.

To demonstrate how the ISP works in our employee data management system, let's say we now need to create a new type of employee called a "contractor". A contractor has all the attributes of a regular employee, but they are paid by the hour instead of a salary. We also want to be able to calculate their total pay based on the number of hours they worked.

To follow the ISP, we should create separate interfaces for employees and contractors that only include the methods they need to implement. Let's create an Employee interface that includes the `get_name`, `get_id_number`, and `get_salary methods`, and a Contractor interface that includes the `get_name`, `get_id_number`, and `calculate_pay` methods.

In the `Employee` interface, we have included the `get_name`, `get_id_number`, and `get_salary` methods that all employees need to implement. In the Contractor interface, we have included the `get_name`, `get_id_number`, and `calculate_pay` methods that only contractors need to implement.

Modifying the `EmployeePrinter` class to use the `Employee` interface and the `ContractorPrinter` class to use the Contractor interface.

In the modified `EmployeePrinter` class, we are using the `Employee` interface to retrieve the name, ID number, and salary attributes. In the `ContractorPrinter` class, we are using the Contractor interface to retrieve the name, ID number, and calculate the pay based on the number of hours worked.

By creating separate interfaces for employees and contractors, we are following the ISP. Clients that only need to work with employees can use the `Employee` interface without being forced to depend on methods they do not use from the Contractor interface. Likewise, clients that only need to work with contractors can use the Contractor interface without being forced to depend on methods they do not use from the `Employee` interface.

This principle promotes the creation of interfaces that are specific to the needs of each client and encourages the development of more flexible and maintainable systems.