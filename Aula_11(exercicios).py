#1
#a)
def areaRetangulo(lado1,lado2):
    area=lado1*lado2
    return area

#b)
def hipotenusa(cateto1,cateto2):
    hipotenusa=(cateto1*cateto1+cateto2*cateto2)**(1/2)
    return hipotenusa

#c)
def areaTotal(a,b,c,d,e):
    area1=areaRetangulo(a,b)
    area2=areaRetangulo(c,d)
    area3=areaRetangulo(e,hipotenusa(a,d))
    area4=areaRetangulo(a,d)/2
    print('Area Retangulo 1:',area1,'Area Retangulo 2:',area2,'Area Retangulo 3:',area3,'Area Triangulo:',area4)
    return area1+area2+area3+area4

#d)
a1=int(input('Valor de a: '))
b1=int(input('Valor de b: '))
c1=int(input('Valor de c: '))
d1=int(input('Valor de d: '))
e1=int(input('Valor de e: '))

area=areaTotal(a1,b1,c1,d1,e1)
print(area)

#6
#a)b)
def acrescimo(nome,numero,sexo):
    if sexo=='f':
        número_com_acréscimo=numero+4
    else:
        número_com_acréscimo=numero+2
    if ('sol' or 'Sol') in nome:
        número_com_acréscimo=número_com_acréscimo+7
    return número_com_acréscimo

def numero_sorte(dia,mes,ano,nome,sexo):
    dia_com_acréscimo=acrescimo(nome,dia,sexo)
    mês_com_acréscimo=acrescimo(nome,mes,sexo)
    soma=dia_com_acréscimo+mês_com_acréscimo+ano
    numero_sorte=soma%10
    return numero_sorte


#c)
nome=input('Nome?')
sexo=input('Sexo?')
estCiv=input('Estado Civil?')
datNas=input('Nascimento no formato dd/mm/aa?')

nSorte=numero_sorte(int(datNas[:2]),int(datNas[3:5]),int(datNas[6:]),nome,sexo)

if estCiv=='c':
    datCas=input('Casamento no formato dd/mm/aa')
    nSorte2=numero_sorte(int(datCas[:2]),int(datCas[3:5]),int(datCas[6:]),nome,sexo)
    if nSorte2>nSorte:
        nSorte=nSorte2
print('O bonus é de: %.2f'%(1000.00*nSorte))


#3
def juntastring(string1,string2):
    return string1[1:]+string2[int(len(string2)-1):0:-1]

j=juntastring('abcd','efghi')

#2
#a)
def descobre_x(ano):
    if ano>=1900 and ano<=2199:
        x=24
    else:
        x=25
    return x

#b)
def descobre_y(ano):
    if ano>=1900 and ano<=2099:
        y=5
    elif ano<=2199:
        y=6
    else:
        y=7
    return y

#c)
def exibe_dia_mes(a,d,e):
    if d+e>9:
        dia=(d+e-9)
        mes=4
        if dia==26:
            dia=26-7
        elif dia==25 and d==28 and a>10:
             dia=18
    else:
        dia=(d+e+22)
        mes=3
    print('Dia:',dia,'Mes:',mes)
    return

ano=2100
x=descobre_x(ano)
y=descobre_y(ano)
a=ano%19
b=ano%4
c=ano%7
d=(19*a+x)%30
e=(2*b+4*c+6*d+y)%7

    
    



        

