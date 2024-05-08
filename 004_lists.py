## listas ##
my_list = list()
my_orther_list = []

print(len(my_list))

my_list = [35, 24, 62, 30, 30, 17]

print(type(my_list))
print(type(my_orther_list))

my_orther_list = [5, 1.77 , "jose", "carcamo"]
print(my_orther_list.count("jose"))

#age, leight, name, sourname = my_orther_list
#print(name)

print(my_list + my_orther_list)

my_orther_list.append("leodev")
print(my_orther_list)

my_orther_list.insert(1, "blanco")
print(my_orther_list)

my_orther_list.remove("blanco")
print(my_orther_list)

my_pop_element = my_orther_list.pop(2)
print(my_pop_element)

del my_list[2]

my_orther_list[2] = "urbina"
print(my_orther_list)

my_new_list = my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)