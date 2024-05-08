## Clases
class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, sourname ,alias = "sin alias") -> None:
        self.name =  name
        self.sourname = sourname
        self.fullname = f"{name} {sourname} **{alias}**"
        self.__hindename = "toto"

    def get_hide_name (self):
        return self.__hindename
        
    def walk(self):
        print(f"{self.fullname}  esta caminando")

my_person =  Person("jose","leonidas")
print(my_person.name)
print(my_person.fullname)
my_person.walk()

my_other_person = Person("moure","brais", "Mouredev")
print(my_other_person.name)
print(my_other_person.fullname)
my_other_person.walk()
my_other_person.fullname = "Jose leonidas"
print(my_other_person.fullname)
print(my_other_person.get_hide_name())

class car:
    def __init__(self, brand, model, year) -> None:
        self.brand =  brand
        self.model =  model
        self.year = year

    def get_all(self):
        return(F"{self.brand} {self.model} {self.year}")

brand = input("ingrese la marca")
model = input("ingrese el modelo")
year =  input("ingrese el years")

my_car =  car(brand,model,year)

print(my_car.get_all())
