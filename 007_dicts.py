### diccionarios ##

my_dict = dict()
my_other_dic ={}

print(type(my_dict))
print(type(my_other_dic))

#clave y valor
my_other_dic = {"Nombre":"jose", 
                "Apellido":"carcamo", 
                "Edad":27, 
                "1":"python"
                }

my_dict = {"Nombre":"jose", 
                "Apellido":"carcamo", 
                "Edad":27, 
                "lemguajes":{"Python","C#","php"}
                }

print(my_other_dic)
print(my_dict)

print(my_dict["Nombre"])
my_dict["Nombre"] = "LEONIDAS"
print(my_dict["Nombre"])

my_dict["direccion"] = "chinandega"
print(my_dict)

del my_dict["direccion"]
print(my_dict)

#Busqueda de clave
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dic =  dict.fromkeys(my_dict)
print(my_new_dic)