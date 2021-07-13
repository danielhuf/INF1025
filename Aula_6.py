import turtle

#definida a função para desenhar um quadrado
'''
def DesenhaQuadrado(tart):
    tart.fd(100)
    tart.lt(90)
    tart.fd(100)
    tart.lt(90)
    tart.fd(100)
    tart.lt(90)
    tart.fd(100)
    tart.lt(90)
    return
'''

#definida a função para desenhar e colorir um quadrado
'''
def DesenhaQuadradoColorido(tart,cor):
    tart.fillcolor(cor)
    tart.begin_fill()
    DesenhaQuadrado(tart)
    tart.end_fill()
    return
'''

#definida a função para deslocar a seta para a direita
'''
def DeslocaDireita(tart):
    tart.up()
    tart.fd(100)
    tart.down()
    return
'''
#Nao necessariamente precisa ser tart para as duas funcoes

#Dois quadrados de cores diferentes são desenhados um do lado do outro
'''
pat=turtle.Turtle()
pat.left(45)
DesenhaQuadradoColorido(pat,'green')
pat.rt(45)
DeslocaDireita(pat)
pat.left(45)
DesenhaQuadradoColorido(pat,'yellow')
'''

#Dois quadrados são desenhados por duas tartarugas diferentes
'''
pat=turtle.Turtle()
pat.shape('turtle')
pat.begin_fill()
pat.fillcolor('green')
pat.lt(45)
DesenhaQuadrado(pat)
pat.end_fill()
alex=turtle.Turtle()
alex.shape('turtle')
alex.begin_fill()
alex.fillcolor('yellow')
alex.lt(45)
alex.up()
alex.goto(40,0)
alex.down()
DesenhaQuadrado(alex)
'''

#Definida a função para desenhar um quadrado tendo a distancia como parametro
'''
def DesenhaQuadrado(tart,dist):
    tart.fd(dist)
    tart.lt(90)
    tart.fd(dist)
    tart.lt(90)
    tart.fd(dist)
    tart.lt(90)
    tart.fd(dist)
    tart.lt(90)
    return
'''

#Definida a função para deslocar para a direita tendo a distancia como parametro
'''
def DeslocaDireita(tart,dist):
    tart.up()
    tart.fd(dist)
    tart.down()
    return
'''

#Quadrados de tamanhos diferentes serão desenhados um do lado do outro
'''
dan=turtle.Turtle()
DesenhaQuadrado(dan,100)
DeslocaDireita(dan,100)
DesenhaQuadrado(dan,50)
DeslocaDireita(dan,50)
DesenhaQuadrado(dan,25)
DeslocaDireita(dan,25)
'''

#Quatro quadrados de lado 200 são desenhados como no formato de uma janela
''''
dan=turtle.Turtle()
DesenhaQuadrado(dan,200)
DeslocaDireita(dan,200)
DesenhaQuadrado(dan,200)
dan.up()
dan.goto(0,200)
dan.down()
DesenhaQuadrado(dan,200)
DeslocaDireita(dan,200)
DesenhaQuadrado(dan,200)
'''

#Definida a função para desenhar uma seta tendo a orientação como parametro
#Quatro tartarugas sao criadas e fazem a seta em 4 orientaçÕes diferentes
def DesenhaUm(tart,orient):
    tart.left(orient)
    tart.fd(100)
    tart.left(120)
    tart.fd(50)
    return

t1=turtle.Turtle()
t1.color('red')
DesenhaUm(t1,90)
t2=turtle.Turtle()
t2.color('blue')
DesenhaUm(t2,180)
t3=turtle.Turtle()
t3.color('green')
DesenhaUm(t3,270)
t4=turtle.Turtle()
t4.color('orange')
DesenhaUm(t4,360)







    
    


