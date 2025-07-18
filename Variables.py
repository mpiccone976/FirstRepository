#Ejercicio 1
first_name = "Matias"
last_name = "Gonzalez"
full_name = first_name + " " + last_name
country = "Uruguay"
city = "Montevideo"
age = 25
year = 2025
is_married = False
is_true = True
is_light_on = True
first_name1, last_name1, country1, age1, is_married1 = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True #varias variables en una sola línea

print("Full Name:", full_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Year:", year)
print("Is Married:", is_married)
print("Is True:", is_true)
print("Is Light On:", is_light_on)
print("")
print(first_name1, last_name1, country1, age1, is_married1)
print("First Name:", first_name1)
print("Last Name:", last_name1)
print("Country:", country1)
print("Age:", age1)
print("Is Married:", is_married1)

# Ejercicio 2
print("")
print(type(first_name1))
print(type(last_name1))
print(type(country1))
print(type(age1))
print(type(is_married1))
print("")
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print("")

print(len(first_name)) #longitud de la cadena string
print(len(last_name))
if len(first_name) > len(last_name):
    print("El nombre es más largo que el apellido")
else:
    print("El apellido es más largo que el nombre")
num_one = 5
num_two = 4 
total = num_one + num_two
difference = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print("Total:", total)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

input("First Name: "), input("Last Name: "), input("Country: "), input("Age: "), input("Is Married: ") #input se utiliza para recibir datos del usuario

help("keywords") #muestra las palabras reservadas de Python 