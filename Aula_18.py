#COMO FAZER LISTAS

#Corrigir 10 questoes de uma prova

l=['Maria',3,15.0,'Joao']
i=0

while i<len(l):
    print(l[i])
    i+=1

#USANDO O FOR

for el in l:    #cria a cada vez a variavel el
    print(el)   #acessa sequencialmente os elementos da lista (do primeiro ao ultimo)


s='Joao e legal'
for l in s:     #ITERAR É USAR O FOR
    print(l)

for i in range(len(l)):
    print(l[i])

for(pos,el) in enumerate(l):   #enumerate caminha sobre o conjunto e forma pares
    print(el,'na posicao',pos)

lista=list(range(3))   #sera de 0 a 2
print(lista)

long=list(range(-3,3,2))   #inicio final e de quanto em quanto
print(long)

lis=random.sample(range(0,100),4)   #4 numeros aleatorios de 0 a 100

#dever

#exibe os elementos da lista um por linha

def porlinha(lista):
    for el in lista:
        print(el)
    return

def soma(lista):    #soma todos os elementos da lista
    acumulador=0
    for el in lista:    #vou testar antes de existe uma sublista dentro da lista (chamarei a funcao novamente)
        if type(el) is int:   #is é equivalente a ==
            acumulador+=el
        else:      #se tiver string fazer elif type(el) is list
            sub=soma(el)
            acumulador+=sub
    return acumulador
        

l1=[3,7,1,90,2]
l2=[3,[98,2,1],10]


porlinha(l1)
porlinha(l2)

print(soma(l1))
print(soma(l2))

import random

def multiplica(lista):
    mult=1
    for el in lista:
        if type(el) is int:
            mult*=el
        else:
            m=multiplica(el)
            mult*=m
    return mult

def contanum(lista):
    cont=0
    for el in lista:
        if type(el) is int:
            cont+=1
        else:
            c=contanum(el)
            cont+=c
    return cont
    
def med(lista):
    c=contanum(lista)
    s=soma(lista)
    return s/c

def maiorvalor(lista):
    maior=-41
    for el in lista:
        if type(el) is int:
            if el>maior:
                maior=el
        else:
            m=maiorvalor(el)
            if m>maior:
                maior=m
    return maior

def substitui(lista):
    for (pos,el) in enumerate(lista):
        if type(el) is int:
            if el%4==0:
                lista[pos]=0   #troca a posicao por 0, nao o el por 0, já que ele muda toda vez que repete o for
        else:
            substitui(el)
    return

def presente(lista):    
    num=int(input('Informe um numero: '))
    for el in lista:
        if type(el) is int:
            if el==num:
                return True
        elif type(el) is list:
            for al in el:
                if type(al) is int:
                    if al==num:
                        return True
    return False
            

lgrande=random.sample(range(-20,20),14)
lgrande[0]=random.sample(range(-10,10),3)
lgrande[4]=random.sample(range(100),2)
lgrande[12]=random.sample(range(-40,16),4)

ldani=[1,[2,8],4]
print(presente(ldani))

