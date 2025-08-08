'''
lenguajes=["php","java","python","javascript"]

print("lenguaje seleccionado: " +lenguajes[2])

lenguajes[2]="c++"

print("lenguaje " + lenguajes[2])

lenguajes.append(("C sharp"))
print(lenguajes)

lenguajes.remove("java")
print(lenguajes)


for x in range (10,20):
    print(x)

for num in range (0,100,5):
    if(num>=75):
        break
    print(num)



for num in range(1,11):
    if(num == 3 or num==6 or num==9):
        continue
    print(num)


#while

inicio=0
fin=10

while(inicio<=fin):
    inicio=inicio+1
    if(inicio==6):
        continue
    print("se repite" + str(inicio))
'''
'''
#funciones sin parametros

def saludo():
    print("hola")
    print("saludos")

print("esto es una funcion")
saludo()
'''
'''
def saludar():
    print("hola")
def salir():
    print("hasta luego")

def suma(a,b):
    resultado=a+b
    print("la suma es: " +   str(resultado))

saludar()
a=input("dame a: ")
b=input("dame b: ")
a=int(a)
b=int(b)
suma(a,b)
'''
'''
def datos(nom,ap,am):
    print("tu nombre :{} {} {}" .format(nom,ap,am))

datos("saul","frias","zamora")

'''
#funcion *args
def suma(*args):
    resultado=0
    for n in args:
        resultado=resultado+n
    print("el resultado es: "+str(resultado))

suma(5,6)