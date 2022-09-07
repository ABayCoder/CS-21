# Kevin Basmadjian
# CS 21
# Program: Video Star

"""
Module description:
This module contains a function that has one for loop nested inside another for
    loop. It creates two number triangles next to each other- one rightside up
    and the other upside down.

"""

def video_star():
    #5 permanent rows, y-axis
    for i in range(5): #main for loop- outer funct
        print(" " * (5 - i), end = "")
        #for j in range(0, num_rows - i): #used hint to get ride of for loop
            #print(end = " ")
        #x-axis, columns equal to 6
        for j in range(6): #inner funct
            if j < i + 1:
            #print normal tree
                print(i, end = " ") #had to change j to i
            #print upside-down tree
            else:
                #diff rows equal to 4
                print(4 - i, end = " ") #had to change j to i
        #print both
        print()
