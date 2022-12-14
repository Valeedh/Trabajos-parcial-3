import turtle
import random

turtle.shape("turtle")    

for i in range (0,4):
    turtle.forward(100)
    turtle.right(90)
for i in range (0,10):
    for i in range( 0,4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(36)
    for i in range (0,10):
        turtle.forward(100)
        turtle.right(36)
    for i in range(0,4):
         turtle.forward(50)
         turtle.right(90)    


turtle.hideturtle( ) 
    
turtle.exitonclick()




