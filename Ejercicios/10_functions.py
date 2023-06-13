### Funciones ###

def my_function ():
    print("Se imprime print de la funcion")

my_function()

def sum_values (one_value, two_value):
    print(one_value + two_value)

sum_values(5,8)

def sum_values_con_return(one_value, two_value):
    sum_resul = one_value + two_value
    return sum_resul

result = sum_values_con_return(7,8)
print(result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Gazcon", name="Daniel")

def print_name(name, surname ,alias="N/A"):
    print(f"{name} {surname} {alias}")

print_name(surname="Gazcon", name="Daniel", alias="ADG")
print_name(surname="Gazcon", name="Daniel")

def parames_infinitos(*text):
    for textos in text:
        mayus = textos.upper()
        return mayus 

my_set = {"Java", "Python", "JavaScript", "AS400", "PHP", "perl", "as400", "shift", "yaml"}
for lenguaje in my_set:
    result = parames_infinitos(lenguaje)
    print(result)