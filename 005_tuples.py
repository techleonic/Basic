my_tuple = tuple()
my_other_tuple = ()
#conjunto de valores

my_tuple= (35, 1.77, "jose", "leonidas")
print(my_tuple)
print(type(my_tuple))

my_other_tuple = (35, 25, 60, 30)
print(my_tuple[1])
print(type(my_tuple))

print(my_tuple.count("jose"))
print(my_tuple.index("leonidas"))

#una tupla los valores no cambian
#my_tuple[1]= 1.80

print(my_tuple + my_other_tuple)

my_tuple =  list(my_tuple)

my_tuple = ["leo",35,36]

print(type(my_tuple))
my_tuple = tuple(my_tuple)

print(type(my_tuple))