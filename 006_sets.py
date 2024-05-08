my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente un diccionario

my_other_set = {"jose", "leonidas", 35}
print(type(my_other_set))

my_other_set.add("leotech")
print(my_other_set) #no es una estructura orenada no se puede accerder on index

my_other_set.add("leotech") #no puede haber repetidos
print(my_other_set)

print("leonidas" in my_other_set)
print("jose" in my_other_set)

my_other_set.remove("jose")
print(my_other_set)

#convertir un set en una lista
my_set = {"jose", "leonidas", 27}
my_list = list(my_set)
print(my_list)
print(my_list[1])

my_other_set = {"C#","php", "python"}

#unir sets
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union({"javascript", "kotlin"}))

print(my_new_set.difference(my_set))