#1

N=int(input('Quantos números? '))
cont=0
quant_dentro=0
soma_dentro=0
quant_fora=0

while cont<N:
    num=int(input('Número? '))
    if 1<=num<=15:
        print('%d está dentro do intervalo'%num)
        quant_dentro+=1
        soma_dentro+=num
    else:
        print('%d está fora do intervalo'%num)
        quant_fora+=1
    cont+=1

if quant_dentro>0:
    media_dentro=soma_dentro/quant_dentro
else:
    media_dentro=0

print('%d valores dentro do intervalo, soma = %d e media = %.1f'%(quant_dentro,soma_dentro,media_dentro))
print('%d valores fora do intervalo'%quant_fora)
        
#2
import random

def defineAtipico(tmedia):
    if tmedia<15 or tmedia>38:
        atipico=True
    else:
        atipico=False
    return atipico

def mediat(a,b):
    return (a+b)/2

dia_mes=1
tminimas=0
tmaximas=0
dias_atipicos=0

while dia_mes<=31:
    t1=random.randint(-10,45)
    t2=random.randint(-10,45)
    media=mediat(t1,t2)
    print('Temperatura média do dia %d = %.1f graus Celsius'%(dia_mes,media))
    if t1<=t2:
        minima=t1
        maxima=t2
    else:
        minima=t2
        maxima=t1
    if defineAtipico(media)==True:
        dias_atipicos+=1
    tminimas+=minima
    tmaximas+=maxima
    dia_mes+=1

media_minimas=tminimas/dia_mes
media_maximas=tmaximas/dia_mes
percent=(dias_atipicos/dia_mes)*100

print('Média das temperaturas mínimas = %.1f graus Celsius'%media_minimas)
print('Média das temperaturas máximas = %.1f graus Celsius'%media_maximas)
print('Percentual de dias atípicos = %.1f %%'%percent)

#3
num_pessoas=int(input('Número de pessoas? '))

cont=1
menor=0
mais20=0
soma_idades=0

while cont<=num_pessoas:
    idade=int(input('Idade da pessoa %.d? '%cont))
    if idade<18:
        menor+=1
    if idade>=20:
        mais20+=1
    soma_idades+=idade
    cont+=1

media=soma_idades/(cont-1)
percent=(mais20/(cont-1))*100

print('Quantidade de pessoas menores de idade = %d'%menor)
print('Média de idade das pessoas = %.1f'%media)
print('Percentual de pessoas com mais de 20 anos = %.2f %%'%percent)
