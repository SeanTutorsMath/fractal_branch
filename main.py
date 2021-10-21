#https://mitpress.mit.edu/books/turtle-geometry

from turtle import *

speed(0)

penup()
rt(-90)
bk(800)
pendown()

angle = 45

def branch(length, level):
    if level > 0:
        
        fd(length)
        
        rt(angle)
        
        branch(0.5 * length, level - 1)
        
        lt(2 * angle)
        
        branch(0.5 * length, level - 1)
        
        rt(angle)
        bk(length)
        
branch(500,7)
        
done()