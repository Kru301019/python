from graphics import*
from time import*

def movingcircle():
    
    win = GraphWin('circle',400,400)
    poi = Point(200,200)
    cir = Circle(poi,50)
    
    cir.setFill('yellow')
    cir.setOutline('green')
    poi.setFill('blue')
    win.setBackground('black')
    cir.draw(win)
    poi.draw(win)
    
    for i in range(200):
        cir.move(20,20)
        sleep(1)
    
    #win.getMouse()
    
movingcircle()    