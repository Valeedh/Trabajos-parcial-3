import random
print("piensa un numero del 1 al 20")
num= random.randint(1,20)

for i in range (0,6):
   choose = int(input("Introduce un numero: "))
   if choose == num:
        correct = True 
        break
   elif choose > num:
      print ("muy alto")
   else:
      print ("muy bajo")




