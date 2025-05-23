class Person:
    def __init__(self, name):
        """Base class constructor"""
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        """Child class constructor"""
        super().__init__(name)  # Calls Person.__init__()
        self.subject = subject

# Create a Teacher object
teacher = Teacher("Ibrahim", "Computer Science")

# Verify initialization
print(f"Teacher: {teacher.name} (Subject: {teacher.subject})")