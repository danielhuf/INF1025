#todas as tabuadas de 1 a 10
def tabuada(n):
    mult=1
    while mult<=10:
        print('%d x %d = %d'%(mult,n,mult*n))
        mult+=1
    return

num=1   #ESTRUTURA DETERMINADA   (existe um contador que vai aumentando ate atingir o limite)
while num<=10:
    print('\n Tabuada do',num)     #\n faz uma nova linha
    tabuada(num)
    num+=1

num=int(input('Qual o numero?'))     #ESTRUTURA INDETERMINADA (pede ao usuario um valor inicial e enquanto atender a necessidade, faz e pergunta novamente)
while num!=0:    #o 0 nesse caso é o FLAG
    tabuada(num)
    num=int(input('Qual o numero?'))

#funcao de transferencia do frasco 1 para o frasco 2
def transfere(frasco1):    #obs:  end=' '   ------> printar o proximo na mesma linha
    frasco2=0
    while frasco1-frasco2>10:    #limite para parar de transferir
        frasco1-=10
        frasco2+=10
        frasco1=frasco1-0.035*frasco1
        frasco2=frasco2-0.012*frasco2
        print('frasco 1 = %2.f e frasco 2 = %2.f'%(frasco1,frasco2))
    return

def valida():
    frasco1=float(input('ml no frasco original?'))
    while frasco1<40 or frasco1>230:
        print('Quantidade inválida')
        frasco1=float(input('ml no frasco original?'))
    return frasco1

frasco1=valida()
transfere(frasco1)

#funcao que mostra a media final de cada aluno. quando a matricula for 0 o programa irá parar. Se qualquer uma das notas nao estar entre 0 e 10, perguntara novamente
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

mat=int(input('Número de matrícula?'))
while mat!=0:
    n=validaNota('Nota da prova?')
    t=validaNota('Media dos trabalhos?')
    media=calculaMedia(n,t)
    print('Media de %d é %.1f'%(mat,media))
    mat=int(input('Número de matrícula?'))
    contmedias+=media    #contadores para no final fazer a media da turma
    nalunos+=1

if nalunos!=0:     #criei uma seguranca para se na primeira vez colocar 0, nao fazer uma media com denominador 0
    mediatotal=contmedias/nalunos
    print('Media da nota da turma = %.1f'%mediatotal)





