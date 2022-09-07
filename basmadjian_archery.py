# Kevin Basmadjian
# CS 21
# Program: Patterns

"""
Module description:
This module creates a colored archery target in a graphics window and assigns
    different values to each color- when the user clicks on an area in the
    graphics window, the module adds up the total amount of points and displays
    it below the target.

"""
#import the graphics set
from graphics import *

def create_target_window():
    #set up the circle- graph the coordinates
    win = GraphWin("Virtual Archery", 600, 600)
    win.setBackground("gray")
    p = Point(250,250)
    
    #white outer circle
    c = Circle(p, 250)
    c.draw(win)
    c.setFill("white")
    #black inner circle
    c2 = Circle(p, 200)
    c2.draw(win)
    c2.setFill("black")
    #blue inner circle
    c3 = Circle(p, 150)
    c3.draw(win)
    c3.setFill("blue")
    #red inner circle
    c4 = Circle(p, 100)
    c4.draw(win)
    c4.setFill("red")
    #yellow inner circle
    c5 = Circle(p, 50)
    c5.draw(win)
    c5.setFill("yellow")

    return win


def main():
    win2 = create_target_window()
    #user starting points equals zero
    userP = 0

    #"Current Score:" is placed below the target
    score = Text(Point(250, 550), "Current Score: 0")
    score.draw(win2) #error here- check if while True indented correctly
    
    while True:
        keystroke = win2.checkKey()
        #when user presses q, the program quits
        if keystroke == "q":
            break
        
        #calculate distance between center point and where user clicked
        p1 = win2.checkMouse()
        if p1:
            X = p1.getX()
            Y = p1.getY()
            distance = abs(((250-X)**2 + (250-Y)**2)**0.5)
            #print distance

            #score 9
            if (distance <= 50):
                userP += 9
                p1.draw(win2)
            #score 7
            elif (distance <= 100):
                userP += 7
                p1.draw(win2)
            #score 5
            elif (distance <= 150):
                userP += 5
                p1.draw(win2)
            #score 3
            elif (distance <= 200):
                userP += 3
                p1.draw(win2)
            #score 1
            elif (distance <= 250):
                userP += 1
                p1.draw(win2)
            #score 0
            elif (distance <= 300):
                userP += 0
                p1.draw(win2)

            #change the score from 0 to the user input
            score.setText("Current Score: " + str(userP))
    #close window when loop is broken
    win2.close()
