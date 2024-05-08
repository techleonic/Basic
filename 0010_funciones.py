## funciones ###

def my_function():
    print("esto es una funcion")

my_function()

def sum (value1, value2):
    print(value1+value2)

sum(5,7)

def sumretrun (value1, value2):
    return value1 + value2

result = sumretrun(10, 5)
print(result)

def print_name (name, sourname):
    print(f"{name} {sourname}")

print_name(name = "leonidas", sourname= "carcamo" )


def print_name_default (name, sourname, alias = "sin alias"):
    print(f"{name}  {sourname} {alias}")

print_name_default("Joese","leonidas")

def print_all_text(*text):
    print(text)

print_all_text("hola", "mundo", "python")

def prit_all_upper (*texts):
    for texto in texts:
        print(texto.upper())

prit_all_upper("hola","python","leo")