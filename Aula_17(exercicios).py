# AGORA VAMOS COMPUTAR A MAIOR NOTA DA TURMA
def calculaMedia(nota,trabalho):
    return 0.8*nota+0.2*trabalho

def validaNota(msg):
    nota=float(input(msg))
    while nota<0 or nota>10:
        print('Digite uma nota valida entre 0 e 10;')
        nota=float(input(msg))
    return nota
    
contmedias=0
nalunos=0
maiorMedia=-1    #se for menor media, começa de 11

mat=int(input('Número de matrícula?'))
while mat!=0:
    n=validaNota('Nota da prova?')
    t=validaNota('Media dos trabalhos?')
    media=calculaMedia(n,t)
    if media>maiorMedia:
        maiorMedia=media
        matrMaiorMedia=mat    #registrei a matricula de quem obteve a maior media
    print('Media de %d é %.1f'%(mat,media))
    mat=int(input('Número de matrícula?'))
    contmedias+=media    #contadores para no final fazer a media da turma
    nalunos+=1

if nalunos!=0:     #criei uma seguranca para se na primeira vez colocar 0, nao fazer uma media com denominador 0
    mediatotal=contmedias/nalunos
    print('Media da nota da turma = %.1f'%mediatotal)
    print('Maior media da turma = %.1f da matrícula %d'%(maiorMedia,matrMaiorMedia))


import random
n=random.randint(-100,100)
contazero=0
somapares=0
menornegativo=0
maiorpositivo=0
somanumeros=0
contnumeros=0

while n!=5:
    if n>0:
        print('Número positivo')
        if n>maiorpositivo:
            maiorpositivo=n
    elif n<0:
        print('Número negativo')
        if n<menornegativo:
            menornegativo=n
    else:
        print('Zero')
    if n%12==0:
        cont=0
        while cont<n:
            print(cont)
            cont+=2
    contazero+=1
    if n%2==0 and n>0:
        somapares+=n
    somanumeros+=n
    contnumeros+=1
    n=random.randint(-100,100)

print('Quantidade de zeros gerada = %d'%contazero)
print('Soma dos numeros pares = %d'%somapares)
print('Menor numero negativo gerado = %d'%menornegativo)
print('Maior numero positivo gerado = %d'%maiorpositivo)
if contnumeros!=0:
    print ('Media dos números = %.1f'%(somanumeros/contnumeros))

def produto_vencido(diavis,mesvis,anovis,diaval,mesval,anoval):
    if anoval<anovis:
        return True
    elif anoval>anovis:
        return False
    elif mesval<mesvis:
        return True
    elif mesval>mesvis:
        return False
    elif diaval<diavis:
        return True
    else:
        return False
    
def calcula_multa(n_conferidos,n_fora):
    percent=(n_fora/n_conferidos)*100
    if percent==0:
        multa=0
    elif percent>30:
        multa=100000
    elif percent>10:
        multa=10000
    else:
        multa=100
    return multa

dvs=int(input('Dia da visita: '))
mvs=int(input('Mes da visita: '))
avs=int(input('Ano da visita: '))
prod=input('Informe o numero do produto: ')
produtos=0
foraval=0

while prod!='':
    dva=int(input('Dia da validade: '))
    mva=int(input('Mes da validade: '))
    ava=int(input('Ano da validade: '))
    if produto_vencido(dvs,mvs,avs,dva,mva,ava)==True:
        print('Está fora da validade')
        foraval+=1
    else:
        print('Está dentro da validade')
    produtos+=1
    prod=input('Informe o numero do produto: ')

c=calcula_multa(produtos,foraval)
if c>0:
    print('Valor da multa = R$%.2f'%c)
        
    


