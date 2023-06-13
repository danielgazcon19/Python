### Sets ###

my_set = set()
my_other_set = set()

my_set = {"Java", "Python", "JavaScript", "AS400", "PHP"}
print(my_set)
my_other_set = {"Daniel", "Gazcon", 34, 1.77}
print(my_other_set)

my_set_union = my_set.union(my_other_set)
print(my_set_union)

other_set = set()
other_set = {34, "C#", ".NET", "Java", "CSS"}
print(other_set)

my_set_union = my_set_union.union(other_set) # No repite valores 
print(my_set_union)

print(my_other_set.difference(other_set))
