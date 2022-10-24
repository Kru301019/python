
from ctypes.wintypes import POINT
from platform import win32_edition
  
from turtle import circle
from graphics import*

from time import*

def drawcircle():
    
    win = GraphWin ('circle',400,400) ##changing default values and giving it a name
    
    #r = float(input('Enter radius'))
    p = Point(100,100)
    c = Circle(p,30) #or circle(p(100,100),30).....30 is radious
    
    
    
    c.setOutline('red')
    c.setFill('blue')
    c.draw(win)
    
    p.draw(win)
    p.setOutline('yellow')
    
    for i in range(10):
        c.move(10,1)
        sleep(1)  #similar thing like get mouse
    
    
    

drawcircle()    