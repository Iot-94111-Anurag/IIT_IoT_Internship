
tonn_to_kg = lambda tonn: tonn * 1000
kg_to_gm = lambda kg: kg * 1000
gm_to_mg = lambda gm: gm * 1000
mg_to_pound = lambda mg: mg * 0.00000220462  # 1 mg = 0.00000220462 lbs


def weight_converter(value, conversion_name, conversion_function):
    result = conversion_function(value)
    print(f"{value} {conversion_name.split('to')[0].strip()} = {result} {conversion_name.split('to')[1].strip()}")
    return result  

# Input in tonnes
tonnes = float(input("Enter weight in tonnes: "))

# Perform sequential conversions
kg = weight_converter(tonnes, "tonn to kg", tonn_to_kg)
gm = weight_converter(kg, "kg to gm", kg_to_gm)
mg = weight_converter(gm, "gm to mg", gm_to_mg)
lbs = weight_converter(mg, "mg to pound", mg_to_pound)
