class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)  # Initialize Person
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Salary: {self.salary}")


class Manager(Employee, Person):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager_info(self):
        print(f"Department: {self.department}")

    def display_full_info(self):
        # Combining behaviors from all classes
        self.display_person_info()
        self.display_employee_info()
        self.display_manager_info()


# Example usage
mgr = Manager("Alice", 35, "E123", 75000, "IT")

mgr.display_full_info()