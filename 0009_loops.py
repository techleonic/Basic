
### loops ###

#while#
my_conditions = 0

while my_conditions < 10:
    print(my_conditions)
    my_conditions += 2
else:
    print("Mi condicion es mayor o igual que 10")

while my_conditions < 20:
    my_conditions += 1
    if my_conditions == 15:
        print("Mi condicion es 15")
        break
    print(my_conditions)

print("La ejecucion continua")


#for#
my_list = [35, 24, 25, 18, 20]
for element in my_list:
    print(element)

my_other_dic = {"Nombre":"jose", 
                "Apellido":"carcamo", 
                "Edad":27, 
                "1":"python"
                }

for element in my_other_dic.values():
    if element == "jose":
        print("Eres tu ")
        break
    print(element)

for element in my_other_dic.values():
    if element == "jose":
        print("Eres tu ")
        continue
    print(element)

