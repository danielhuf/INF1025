#calcular sensacao termica
def sensacaotermica(v,T):
    st=33+(10+v**0.5+10.45-v)*(T-33)/22
    return st

temp=float(input('Qual temperatura? '))
vel=float(input('Velocidade? '))
st=sensacaotermica(temp,vel)
print('A sensacao termica é: %.2f'%st)

#calcular sensacao termica COM WHILE
def sensacaotermica(v,T):
    st=33+(10+v**0.5+10.45-v)*(T-33)/22
    return st

jafiz=0                             #ou jafiz é 0 e <24 ou jafiz é 1 <=25
while  jafiz<24:
    temp=float(input('Qual temperatura? '))
    vel=float(input('Velocidade? '))
    st=sensacaotermica(temp,vel)
    print('A sensacao termica é: %.2f'%st)
    jafiz=jafiz+1   #ir somando até chegar a 24   #se nao soma nada, entra em loop

n=int(input('quantas medicoes foram realizadas'))
jafiz=0
while jafiz<n:
'''
'''
def litrospordia(p):
    return 35*p/1000

def processaTurma(n):
    n=int(input('Quantidade de alunos na turma = '))
    alunos=0
    conta2L=0
    totlitros=0

    while alunos<n:
        peso=float(input('Peso? '))
        l=litrospordia(peso)
        if l>2:
            conta2L=conta2L+1
        totlitros=totlitros+l
        print('Precisa de %.1f litros'%l)
        alunos=alunos+1

    print('Numero de alunos que precisam consumir mais de de deois litros =',conta2L)    #vem fora do while
    print('Total de litros que a turma consome = %.1f'%totlitros)
    media=totlitros/n
    print('Consumo médio por aluno = %.1f',%media)
    return totlitros

# a=a+b é a mesma coisa que a+=b    a*=3  é igual a=a*3

totlitrosGeral=0
nturma=0
while nturmas<5:
    n=int(input('Quantos alunos na turma'+str(nturma+1)))   #nturma+1, porque a turma 0 é a turma 1
    t=processaTurma(n)
    totlitrosGeral+=t
    nturma+=1

print('O total de litros das turmas é %.1f'%totlitrosGeral)

def exibeCaracteristico(n):
    inc=n//100+n%100
    if inc**2==n:
        print(n)
        return 1
    else:
        return 0

cont=0
num=1000
while num<=9999:
    s=exibeCaracteristico(num)
    cont+=s
    num+=1

print('Quantidade de numeros com essa caracteristica =',cont)
    
    
    
    
