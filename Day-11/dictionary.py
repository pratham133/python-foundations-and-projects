# Program 1 (Create a Dictionary)

student = {
    "name": "Pratham",
    "age": 22,
    "city": "Mumbai"
}

print(student)


# Program 2 (Access Dictionary values)

student = {
    "name": "Pratham",
    "age": 22,
    "city": "Mumbai"
}

print(student["name"])
print(student["age"])
print(student["city"])


# program 3 (Print sentence from Dictionary)

student = {
    "name": "Pratham",
    "age": 22,
    "city": "Mumbai"
}

print(f"My name is {student['name']}")
print(f"I am {student['age']} years old")
print(f"I live in {student['city']}")


# Program 4 (Update Dictionary Value)

car = {
    "brand": "BMW",
    "color": "Black",
    "model": "X5"
}

car["color"] = "Matte Black"

print(car)


# Program 5 (Add new key-value pair in)

car = {
    "brand": "BMW",
    "color": "Matte Black",
    "model": "X5"
}

car["year"] = 2024

print(car)


# Program 6 (Delete Key-Value pair)

car = {
    "brand": "BMW",
    "color": "Matte Black",
    "model": "X5",
    "year": 2024
}

del car["year"]

print(car)


# Program 7 (Student Dictionary Practice)

student = {
    "name": "Pratham",
    "age": 21,
    "city": "Mumbai"
}

print("Original dictionary:", student)

student["age"] = 22
print("After updating age:", student)

student["course"] = 'Python'
print("After adding course:", student)

del student["city"]
print("After removing city:", student)

print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")
print(f"Student course: {student['course']}")

