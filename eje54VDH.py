import random
#54
coin = random.choice(  [ "h", "t"]  )
adivina = input ("Ingrese (h)eads o (t)ails: ")
if adivina == coin:
    print("GANASTE")
else:
    print("MALA SUERTE")
if coin == "h":
    print ("Fue heads")
else:
    print ("Fue tails")  