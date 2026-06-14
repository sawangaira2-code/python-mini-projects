# Employee Management System

class Employee:
    def __init__(self, name, salary):
        # Store employee name and salary
        self.name = name
        self.salary = salary

    def display(self):
        # Display employee details
        print("Name:", self.name)
        print("Salary:", self.salary)

    def salary_status(self):
        # Check whether salary is good or low
        if self.salary >= 20000:
            print("Good Salary")
        else:
            print("Low Salary")


e1 = Employee("Sawan", 25000)

e1.display()
e1.salary_status()
