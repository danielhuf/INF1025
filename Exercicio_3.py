#1 e)
import turtle
dan=turtle.Turtle()


dan.up()
dan.circle(100,30)  #o raio é 100, porem para de desenhar no 30
dan.down()
dan.circle(100,120)
dan.up()
dan.circle(100,240)
dan.lt(120)
dan.down()
dan.circle(-100,120)


#2
def triangulo(tart,dist):
    tart.fd(dist/2)
    tart.lt(120)
    tart.fd(dist)
    tart.lt(120)
    tart.fd(dist)
    tart.lt(120)
    tart.fd(dist/2)
    tart.up()
    tart.lt(90)
    tart.fd(dist/10)
    tart.rt(90)
    tart.down()
    return

def dois_triangulos(tart,dist1,dist2):
    triangulo(tart,dist1)
    triangulo(tart,dist2)
    tart.up()
    tart.rt(90)
    tart.fd((dist2)/10)
    tart.fd((dist1)/10)
    tart.lt(90)
    tart.down()
    tart.fd((dist1)/2)
    return

'''
dan.lt(45)
dois_triangulos(dan,100,70)
dan.rt(90)
dan.fd(50)
dois_triangulos(dan,100,70)
dan.rt(90)
dan.fd(50)
dois_triangulos(dan,100,70)
dan.rt(90)
dan.fd(50)
dois_triangulos(dan,100,70)
dan.rt(90)
'''

#3 a)
def desenhaCirculo(tart,cor,raio):
    tart.fillcolor(cor)
    tart.begin_fill()
    tart.circle(raio)
    tart.end_fill()
    return

def mudaPosicao(tart,dist_vertical):
    tart.up()
    tart.goto(0,dist_vertical)
    tart.down()
    return

'''
desenhaCirculo(dan,'red',50)
mudaPosicao(dan,10)
desenhaCirculo(dan,'white',40)
mudaPosicao(dan,20)
desenhaCirculo(dan,'red',30)
mudaPosicao(dan,30)
desenhaCirculo(dan,'white',20)
mudaPosicao(dan,40)
desenhaCirculo(dan,'red',10)
'''

# b)
'''
desenhaCirculo(dan,'black',50)
dan.up()
dan.goto(-50,75)
dan.down()
desenhaCirculo(dan,'black',25)
dan.up()
dan.goto(50,75)
dan.down()
desenhaCirculo(dan,'black',25)
'''

# c)
'''
def desenhaLinha(tart,comprimento,cor,espessura):
    tart.color(cor)
    tart.width(espessura)
    tart.fd(comprimento)
    return

dan.lt(90)
desenhaLinha(dan,50,'red',5)
dan.rt(90)
dan.up()
dan.goto(-50,0)
dan.down()
dan.circle(25)
dan.up()
dan.goto(50,0)
dan.down()
dan.circle(25)
'''

#4 a)
def linha(tart,tamanho):
    tart.fd(tamanho)
    tart.bk(tamanho*2)
    tart.fd(tamanho)
    tart.rt(90)
    tart.fd(tamanho)
    tart.bk(tamanho*2)
    tart.fd(tamanho)
    tart.lt(90)
    return

'''
linha(dan,50)
'''

# b)
'''
dan.lt(90)
linha(dan,50)
dan.lt(45)
linha(dan,25)
'''

# c)
'''
dan.lt(90)
linha(dan,50)
dan.lt(30)
linha(dan,25)
dan.lt(30)
linha(dan,25)
'''

#6
def circulo(tart,x,y,raio,cor):
    tart.up()
    tart.setposition(x,y-raio)
    tart.down()
    tart.begin_fill()
    tart.fillcolor(cor)
    tart.circle(raio)
    tart.end_fill()
    return

def quadrado(tart,x,y,lado,cor):
    tart.up()
    tart.goto(x,y)
    tart.lt(45)
    tart.fd(lado/2*2**0.5)
    tart.setheading(0)
    tart.fillcolor(cor)
    tart.begin_fill()
    tart.rt(90)
    tart.fd(lado)
    tart.rt(90)
    tart.fd(lado)
    tart.rt(90)
    tart.fd(lado)
    tart.rt(90)
    tart.fd(lado)
    tart.rt(90)
    tart.end_fill()
    tart.down()
    return

'''
lado=70
raio=35
circulo(dan,raio,0,raio,'black')
circulo(dan,0,raio,raio,'black')
circulo(dan,0,-raio,raio,'black')
circulo(dan,-raio,0,raio,'black')
circulo(dan,0,0,lado*(2**(1/2))/2,'white')
quadrado(dan,0,0,lado,'blue')
'''
    

