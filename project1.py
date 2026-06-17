

name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
favno = input("Enter your favorite number: ")
# convert values
age1 = int(age)
height1 = float(height)
favno1 = float(favno)
# calculate birth year
current_year = 2026
birth_year = current_year - age1
print("Birth year:", birth_year)
# variable details
print(f"Name: {name} | Type: {type(name)} | Memory Address: {id(name)}")
print(f"Age: {age1} | Type: {type(age1)} | Memory Address: {id(age1)}")
print(f"Height: {height1} | Type: {type(height1)} | Memory Address: {id(height1)}")
print(f"Fav No: {favno1} | Type: {type(favno1)} | Memory Address: {id(favno1)}")






 