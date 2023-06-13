### Loops ###
# While
my_list = ["Daniel", "Gazcon", "Go", "Mar", "tre", 1, 8, 2 ]
my_condition = 0
can_my_list = len(my_list)
print(can_my_list)

# While
recorrido = my_list[0]
while recorrido != 8:
    my_condition += 1
    recorrido = my_list[my_condition]
    print("Entro al while")
else:
    print("Fuera del while")

# For

for datos in my_list:
    print(datos)
    if datos == "Go":
        print("Sale del FOR my_list")
        break
else:
    print("Bucle FOR list............................")

my_tuple = (35, 1.77, 'Daniel', 'Gazcon')
for datos in my_tuple:
    print(datos)
else:
    print("Bucle FOR tuple............................")

my_set = {"Java", "Python", "JavaScript", "AS400", "PHP"}
for datos in my_set:
    print(datos)
else:
    print("Bucle FOR set............................")

my_dict = {"Nombre":"Daniel", "Apellido":"Gazcon", "Edad":34, 1:"Python", 2:"Java"} 
for datos in my_dict.values():
    print(datos)
    if datos == 34:
        continue # no sirve de ni mierda


else:
    print("Bucle FOR dict............................")