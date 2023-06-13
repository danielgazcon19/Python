### Diccionarios ###
my_dict = dict()
print(type(my_dict))
my_other_dict = {}
print(type(my_other_dict))

my_other_dict = {"Nombre":"Daniel", "Apellido":"Gazcon", "Edad":34, 1:"Python", 2:"Java"} # cada valor se declara con llaves

my_dict = {
    "Nombre":"Daniel",
    "Apellido":"Gazcon",
    "Edad":34,
    "Lenguajes": {
        "Python",
        "Java",
        "PHP"
    }
}

print(len(my_other_dict)) # cantidad de claves
print(len(my_dict)) # cantidad de claves

print(my_dict["Lenguajes"])

my_dict["Lenguajes"] = {"HTML", "CSS", "Ruby"}
print(my_dict)
my_dict["Lenguajes"].add("Python")

print(my_dict)