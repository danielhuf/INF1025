#Daniel Stulberg Huf turma 33D matricula 1920468

import turtle
dan=turtle.Turtle()

#1
def desenhaRetangulo(tart,cor,dist1,dist2):
    tart.color(cor)
    tart.fd(dist1)
    tart.rt(90)
    tart.fd(dist2)
    tart.rt(90)
    tart.fd(dist1)
    tart.rt(90)
    tart.fd(dist2)
    tart.rt(90)
    return

def desloca(tart,dist):
    tart.up()
    tart.fd(dist)
    tart.down()
    return

dan.shape('turtle')
dan.width(2)
dan.lt(180)
desenhaRetangulo(dan,'black',100,50)
dan.rt(180)
desloca(dan,100)
dan.lt(180)
desenhaRetangulo(dan,'brown',100,50)
desloca(dan,100)
dan.lt(90)
desloca(dan,50)
dan.rt(90)
desenhaRetangulo(dan,'yellow',100,50)
dan.rt(180)
desloca(dan,100)
dan.lt(180)
desenhaRetangulo(dan,'blue',100,50)










    
