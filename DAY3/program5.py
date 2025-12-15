# Default Parameter Values in Functions
def greet(name="User", message="Welcome"):
    print(message, name)

# Function calls
greet("Anurag", "Hello")     # Both arguments passed
greet("Anurag")              # message takes default value
greet()                      # both parameters take default values

# Keyword Arguments (key = value)

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

# Keyword arguments
student_info(age=20, course="Python", name="Anurag")

 # Passing Function as an Argument

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operation, x, y):
    result = operation(x, y)
    print("Result:", result)

# Passing function as argument
calculate(add, 10, 5)
calculate(subtract, 10, 5)
