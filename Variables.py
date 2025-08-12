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

input("First Name: "), input("Last Name: "), input("Country: "), input("Age: "), input("Is Married: ") #input se utiliza para recibir datos del usuario

help("keywords") #muestra las palabras reservadas de Python 
print("")

# int to float
num_int = 10
print("num_int:",num_int)         # 10
num_float = float(num_int)
print("num_float:", num_float)   # 10.0
print("")

# float to int
gravity = 9.81
print("Gravity:", int(gravity))             # 9
print("")

# int to str
num_int = 10
print("num_int:", num_int)                  # 10
num_str = str(num_int)
print("num_str:", num_str)                  # "10"
print("")

# str to int or float
num_str = "10.6"
num_float = float(num_str)
print("num_float", float(num_str))  # 10.6
num_int = int(num_float)
print("num_int", int(num_int))      # 10
print("")

# str to list
first_name = "Asabeneh"
print("First_Name:", first_name)               # "Asabeneh"
first_name_to_list = list(first_name)
print("First_Name_to_List:", first_name_to_list)            # ["A", "s", "a", "b", "e", "n", "e", "h"]