
import imp
from turtle import circle
from graphics import*
from time import*

def movingcirlce():
    
    Win = GraphWin('movingCircle')
    circ = Circle(Point(0,0),50)
    
    circ.setFill('blue')
    circ.draw(Win)
    
    for i in range(200):
     circ.move(20,20)
     sleep(1)

    #Win.getMouse() 
    

movingcirlce()    
