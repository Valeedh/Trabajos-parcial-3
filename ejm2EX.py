listanumeros = [] #lista vacia 
respuesta = "<"

while respuesta == "<":
    listanumeros.append int(input("ingresa el numero: ")) #agregar el num al final de la lista 
    print (listanumeros) #muestra la lista

    respuesta = input ("presiona < para agregar otro numero a la lista: ")


print(listanumeros)



