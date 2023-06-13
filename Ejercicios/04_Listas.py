### Listas ###

my_list = list() # forma 1 de definir una lista
my_other_list = [] # forma 2 de definir una lista

print(len(my_list))

my_list = [34, 30 ,20, 15, 45, 17, 60]
print(my_list)
print(len(my_list))

my_other_list = [34, 1.77, 'Daniel', 'Gazcon'] # sepuede combinar tipos de datos
print(my_other_list)
print(my_other_list[1]) # imprimir una posicion de la lista
print(my_other_list[-3]) # imprimir una posicion de la lista de atras adelante
print(my_other_list.count('60')) # imprimir una posicion de la lista

age, height, name, surname = my_other_list
print(name)
 # Operaciones con la lista

my_other_list.append('Desarrollador') # inserta en la ultima posicion
print(my_other_list)

my_other_list.insert(2, "Rojo") # inserta en la posicion que se indique
print(my_other_list)

my_other_list[2] = "Azul"  # modifica el valor de una posicion
print(my_other_list)

my_other_list.remove("Azul") #elimina un elemento
print(my_other_list)

del my_other_list[2] #eliminar un elemento en espeficifoc
print(my_other_list)

my_new_list = my_list.copy() #copia lista
my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() # alreverse
print(my_new_list)

my_new_list.sort() # ordena con numeros de manor a mayor
print(my_new_list)
