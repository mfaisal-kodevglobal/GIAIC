class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def get_info(self):
        return f"Employee {self.emp_id}: {self.name}"

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # Aggregation: Department has references to Employees
    
    def add_employee(self, employee):
        """Add an existing Employee to the department"""
        self.employees.append(employee)
    
    def list_employees(self):
        print(f"Employees in {self.dept_name} department:")
        for emp in self.employees:
            print(f"- {emp.get_info()}")

# Create standalone Employee objects
emp1 = Employee("Ali Raza", "E1001")
emp2 = Employee("Ahmed Ali", "E1002")

# Create a Department
hr_dept = Department("Human Resources")

# Add existing employees to department (aggregation)
hr_dept.add_employee(emp1)
hr_dept.add_employee(emp2)

# List department employees
hr_dept.list_employees()

# Employees continue to exist independently
print("\nStandalone employee access:")
print(emp1.get_info())  # Still accessible outside department