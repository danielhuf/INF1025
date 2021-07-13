#Daniel Stulberg Huf turma 33D matricula 1920468

#mmagagninr@gmail.com

#1
numDias=int(input('Numero de dias do evento: '))
semanas=numDias//7
dias=numDias%7

print(semanas,'semanas e',dias,'dias')

#2
data=input('Escreva uma data: ')
dia=data[:2]
mes=data[6:9]
ano=data[-4:]
data_abreviada=dia+'/'+mes+'/'+ano
print(data_abreviada)
         
#3  
def media(n1,n2):
    mediafinal=((n1)*3+(n2)*7)/10
    return mediafinal

nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))

a=media(nota1,nota2)

print('Média calculada:%2.f'%a)

#4
#a)
import math

def vcaixa(a,b,c):
    return a*b*c

#b)
def vcilindro(r,h):
    return math.pi*h*(r**2)


#c)

comprimento=float(input('Comprimento da caixa: '))
largura=float(input('Largura da caixa: '))
altura=float(input('Altura da caixa: '))
diametro=float(input('Diametro do cilindro: '))

vtotal=vcaixa(comprimento,largura,altura)-vcilindro(diametro/2,altura)

print('Volume Calculado:%3.f'%vtotal)
    


