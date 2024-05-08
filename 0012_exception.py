##Exception.
numberone = 5
numbretwo = 1
numbretwo = "1"

try:
    print(numberone + numbretwo)
    print("no hay eror")
except:
    print("se a producido un eror")

#else
try:
    print(numberone + numbretwo)
    print("no hay eror")
except:
    print("se a producido un eror")
else:
    print("la ejecucion continua correctamente")

#finally
try:
    print(numberone + numbretwo)
    print("no hay eror")
except:
    print("se a producido un eror")
else:
    print("la ejecucion continua correctamente")
finally:
    print("la ejecucion continua")

# Eceptiones por tipo
try:
    print(numberone + numbretwo)
    print("no hay eror")
except ValueError:
    print("se a producido value eror")
except TypeError:
    print("Eror tipo type eror")

#Exceptions captura de informacion
try:
    print(numberone + numbretwo)
    print("no hay eror")
except ValueError as eror:
    print(eror)
except Exception as eror:
    print(str(eror))

