# Declarando variables y organizando datos
num_one = 5
num_two = 4 
# Operaciones aritméticas
total = num_one + num_two
difference = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
# Imprimiendo resultados de las operaciones
print("Total:", total)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

print("")
# Calculando el área de un círculo
radio = 5
area_circulo = 3.14159 * radio ** 2
print("Área del círculo:", area_circulo)

print("")
#Calculando el área de un rectángulo
largo = 10
ancho = 20
area_rectangulo = largo * ancho
print("Área del rectángulo:", area_rectangulo)

print("")
# Calculando el peso de un objeto
masa = 75
gravedad = 9.81
peso = masa * gravedad
print("Peso del objeto:", peso)

# Comparaciones y operadores lógicos
print("")
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('b in Asabeneh', 'b' in 'Asabeneh') # True - there is a lowercase b
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Operadores lógicos
print("")
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True:', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False