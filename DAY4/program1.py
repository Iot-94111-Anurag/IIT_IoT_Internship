def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def feet_to_inch(feet):
    return feet * 12

def inch_to_cm(inch):
    return inch * 2.54


def distance_converter(distance, conversion_type, conversion_function):
    result = conversion_function(distance)
    
    print(
    f"{distance} {conversion_type.split('to')[0].strip()} = "
    f"{result} {conversion_type.split('to')[1].strip()}"
)


distance = float(input("Enter The Distance: "))

distance_converter(distance, "km_to_m", km_to_m)
distance_converter(distance, "m_to_cm", m_to_cm)
distance_converter(distance, "cm_to_mm", cm_to_mm)
distance_converter(distance, "feet_to_inch", feet_to_inch)
distance_converter(distance, "inch_to_cm", inch_to_cm)


