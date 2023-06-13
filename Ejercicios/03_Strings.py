## string ##

my_string = "Mi String"
my_other_string = 'Mi other String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_string_line = "Este es un string\ncon salto de linea"
print(my_string_line)

my_tab_line = "\tEste es un string con tabulacion"
print(my_tab_line)

# Formateo

name, surname, age = "Daniel", "Gazcon", 34

print("Mi nombre es {} {} y tengo {} años de edad".format(name,surname,age))
print("Mi nombre es %s %s y tengo %d años de edad" %(name,surname,age))
print("Mi nombre es" + name + " " + surname + " " + "y tengo" + str(age) + " " + "años de edad")
print(f"Mi nombre es {name} {surname} y tengo {age} años de edad")

# Desempaquetado de Caracteres

lenguaje = 'python'
a,b,c,d,e,f = lenguaje
print(a)
print(e)

# Division

lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

# Reverse

reverse_lenguaje = lenguaje[::-1]
print(reverse_lenguaje)

# Funciones

print(lenguaje.capitalize()) # primera en mayus
print(lenguaje.upper()) #todo en mayus
print(lenguaje.count("t"))
print(lenguaje.isnumeric())
print(lenguaje.lower()) # todo en mninus
print(lenguaje.upper().isupper())
print(lenguaje.lower()) # todo en mninus
print(lenguaje.lower().islower())
