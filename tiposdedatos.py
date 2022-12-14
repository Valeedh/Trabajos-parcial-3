#import random
#posicion = random.randint(0,3)
#tuples
#frutas = (posi0, posi1, posi2, posi3)
#frutas = ("apple", "banana", "strawberry", "orange")

#print(frutas[posicion])

#print(frutas.index("orange"))

alumnos = ("Vale","Niky","Emi","Danna")
##alumnos = ["Vale", 1.66, "femenino", 16,["Español", "informatica"]]
#noLista = int(input("A quien quieres invocar:"))
#print(alumnos[noLista])
##]print(alumnos)
##alumnos.append(input("Esribe al nuevo integrante:"))
##print(alumno[4][1])

listanumeros = [] #lista vacia 
respuesta = ">"

while respuesta == ">":
    listanumeros.append(input("ingresa el nombre del numero: ")) #agregar el num al final de la lista 
    print (listanumeros) #muestra la lista

    respuesta = input ("presiona > para agregar otro numero a la lista: ")

listanumeros.sort()
print(listanumeros)
