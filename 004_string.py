my_string = "Mi string"

my_other_string = "my other string"

my_string_line_string ="Este es u string \n con saltor de linea"

my_string_tab = " \t este es un sting con tabulador"


name, sourname, edad = "jose", "leonidas", 27

#formating of strings
print("Minombre es %s %s y edad es %d" %(name,sourname,edad))
print("Mi nombre es  {} {} y edad es {}".format(name,sourname,edad))
print(f"Mi nombre es  {name} {sourname} y edad es {edad}")

#desenpaquetado
language = "Python"
a, b, c, d, e, f = language
print(a)
print(d)

language_slice = language[1:3]
print(language_slice)



language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#REVERSE
language_slice = language[::-1]
print(language_slice)

#METODOS FUNCIONES DEL SISTEMA

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.lower().isupper())
print(language.startswith("py"))