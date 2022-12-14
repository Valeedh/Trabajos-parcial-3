import random
#55
num = random.randint(1,5)
print(num)
adivina = int(input("introduce un numero:"))
if adivina == num:
    print("Bien hecho")
elif adivina > num:
    print ("muy alto")
    adivina = int(input("Adivina de nuevo: "))
    if adivina == num:
        print("CORRECTO")
    else:
        print("PERDISTE")
elif adivina < num:
    print("muy bajo")     
    adivina = int(input("Adivina de nuevo:"))
    if adivina == num:
        print("CORRECTO")
    else:
        print("PERDISTE")
