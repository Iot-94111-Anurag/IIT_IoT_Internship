

radius = float(input("Enter the radius of circle: "))
length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))

def function1():
    from geometry import Area_Of_Circle, Area_Of_Rectangle

    print(f"Area of circle = {Area_Of_Circle(radius)}")
    print(f"Area of rectangle = {Area_Of_Rectangle(length, breadth)}")

function1()
