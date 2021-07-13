import turtle

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

dan=turtle.Turtle()
dan.shape('turtle')
dan.width(2)
dan.lt(180)
desenhaRetangulo(dan,'black',100,50)
desloca(dan,-50)
desenhaRetangulo(dan,'brown',100,50)
dan.lt(90)
desloca(dan,50)
dan.rt(90)
desenhaRetangulo(dan,'blue',100,50)
desloca(dan,50)
desenhaRetangulo(dan,'yellow',100,50)

#2
def ladoQuad(perimetro):
    return perimetro/4

def diagonalQuad(ladoQuad):
    return ladoQuad*(2**(1/2))

def metade(medida):
    return medida/2

tat=turtle.Turtle()
tat.color('blue')
tat.fd(ladoQuad(160))
tat.lt(90)
tat.fd(ladoQuad(160))
tat.lt(90)
tat.fd(ladoQuad(160))
tat.lt(90)
tat.fd(ladoQuad(160))
tat.lt(90)
tat.fd(metade(ladoQuad(160)))
tat.color('red')
tat.circle(metade(ladoQuad(160)))
tat.up()
tat.fd(metade(ladoQuad(160)))
tat.down()
tat.lt(45)
tat.circle(metade(diagonalQuad(ladoQuad(160))))




    
