# ==========================================
# Program 1 (Public Attributes)
# ==========================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Pratham", 22)

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")


# ==========================================
# Program 2 (Protected Attributes)
# ==========================================

class student:

    def __init__(self,name, age):

        self._name = name
        self._age = age

student1 = student("Pratham", 22)

print(student1._name)
print(student1._age)

# ==========================================
# Program 3 (Private Attributes)
# ==========================================

class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

student1 = Student("Pratham", 22)

print(student1._Student__name)  #Name Mangling to access the __name
print(student1._Student__age)   #Name Mangling to access the __age


# ==========================================
# Program 4 (Getter Methods)
# ==========================================

class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get__age(self):
        return self.__age

student1 = Student("Pratham", 22) 

print(student1.get_name())
print(student1.get__age())


# ==========================================
# Program 5 (Setter Method)
# ==========================================

class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
            print("Age updated successfully!")
        else:
            print("Invalid age!, Age must be greater than 0")

student1 = Student("Pratham", 22)

print(f"Before Update: {student1.get_age()}")

student1.set_age(23)

print(f"After Update: {student1.get_age()}")

student1.set_age(-22)

print(f"Final Age: {student1.get_age()}")