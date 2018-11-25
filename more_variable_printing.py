import sys
print(sys.version)

name = 'Zed A. Shaw'
age = 35
height = 74 * 2.54
weight = 180/2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'



print(f"Let's talk about {name}.")

print(f"He's {height} centimeter tall.")

print(f"He's {round(weight, 2)} kilograms heavy.")

print(f"Actually that's not too heavy.")

print(f"He's got {eyes} eyes and {hair} hair.")

print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight

print(f"If I add {age}, {height}, and {round(weight,2) } I get {round(total,2) }.")
