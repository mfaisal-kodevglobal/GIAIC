class Student:
    def __init__(self, name, marks):
        # Using self to initialize instance variables
        self.name = name
        self.marks = marks
    
    def display(self):
        # Using self to access instance variables
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

student1 = Student("Alice", 95)
student1.display()

student2 = Student("Bob", 87)
student2.display()