# print("Hola, Python")

my_string: str = "Esta es una variable"
print(type(my_string))
print(my_string)

my_string = 8
print(type(my_string))
print(my_string)

my_int = 11
print(type(my_int))
print(my_int)
my_int = my_int + 5
print(my_int)
print(type(8000))

my_float = 7.5
print(type(my_float))
print(my_float)
print(type(10.5))

my_bool = True
print(type(my_bool))
print(my_bool)

# combinar #
# print("Lo valosres de mis variables son: Entero es " + my_int + "Decimal es"  + my_float + "Boolean es " + my_bool) # ERROR

print("Los valosres de mis variables son: Entero es " + str(my_int) + " Decimal es "  + str(my_float) + " Boolean es " + str(my_bool)) #ejemplo con transformacion
print(f"Los valosres de mis variables son: Entero es  {my_int}, Decimal es {my_float} Boolean es {my_bool}") #ejemplo con interpolacion de valores en

# Variables e n una sola linea

name, lastname, age, alias = "Daniel", 'Gazcon', 34, 'danielgazcon19'
print('M nombre es:', name, lastname, 'Mi edad es:',age, 'años', 'y mi alias es:', alias )
# LIstas

my_list = [my_string, my_int, my_float, my_bool]
print(type(my_list))
print(my_list) # imprimri toda la lista
print(my_list[0]) #imprimir una posision de la lista

#estructura diccionario
#diccionario
my_dic = {"string": my_string, "intero": my_int, "float": my_float, "bool": my_bool}
print(type(my_dic))
print(my_dic) 

#set
my_set = {my_string, my_int, my_float, my_bool, my_bool, my_bool}
print(type(my_set))
print(my_set) 

#tuple
my_tuple = (my_string, my_int, my_float, my_bool, my_bool, my_bool)
print(type(my_tuple))
print(my_tuple) 

# Funciones

#print(len(my_int))

#Operadores

if my_int == 16 and my_bool == True:
    print("El resultado es verdadero")
elif my_bool == False:
    print("El resultado es a medias")
else:
    print("EL resultado es falso")

for my_item in my_list: #recorreo todo el contenido
    print(my_item)

for my_item in range(10):
    print(my_item)

