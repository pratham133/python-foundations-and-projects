# ==========================================
# Program 1 (Class Variables)
# ==========================================

class Student:

    college = "ABC University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Pratham", 22)
student2 = Student("Swati", 19)

print(f"Using class: {Student.college}")
print(f"Using student1: {student1.college}")
print(f"using studnet2: {student2.college}")


# ==========================================
# Program 2 (Updating Class Variable)
# ==========================================
   
Student.college = "OpenAI University"

print("\nAfter updating class variable\n")

print(f"Using class: {Student.college}")
print(f"Using student1: {student1.college}")
print(f"Using student2: {student2.college}")


# ==========================================
# Program 3 (Instance Variable Shadows Class Variable)
# ==========================================

student1.college = "MIT"

print("\nAfter changing student1 college:\n")

print(f"Using class: {Student.college}")
print(f"Using student1: {student1.college}")
print(f"Using student2: {student2.college}")


# ==========================================
# Program 4 (Class Method)
# ==========================================

class Student:

    college = "OpenAI University"

    @classmethod
    def show_college(cls):
        print(f"College: {cls.college}")

student1 = Student()
student2 = Student()

Student.show_college()


# ==========================================
# Program 5 (Static Method)
# ==========================================

class Student:
    
    @staticmethod
    def is_valid_age(age):
        return age > 0
    
student1 = Student()

print(Student.is_valid_age(22))
print(Student.is_valid_age(-10))