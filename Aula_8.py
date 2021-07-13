'''
def converte(tempo):
    h=tempo//60
    m=tempo%60
    tempo=str(h)+'h'+str(m)+'min'
    return tempo

def porcentagem(tR,tP):
    p=tR/(tR+tP)*100
    return str(p)

def exibeMensagem(d,tR,tP,p):
    print('Dept %s Tempo em reuniao:%s Em projeto:%s %s  em reuniao'%(d,tR,tP,p))
    return

depto='Fisica'
treu=190
tproj=40

tReu=converte(treu)
tProj=converte(tproj)
porc=porcentagem(treu,tproj)

exibeMensagem(depto,tReu,tProj,porc)
'''

'''
num=input('Digite um numero')
idade=int(input('Digite sua idade'))
'''

def IMC (massa,altura):
    return massa/(altura**2)
def exibe (n,i,a,p,imc):
    print('Nome:',n)
    print('Idade:%3d'%i)
    print('Altura:%4.2f'%a)
    print('Peso:%5.1f'%p)
    print('IMC:%4.1f'%imc)
    return

#Primeiro, através do input, irá aparecer essas expressões, onde eu poderei escrever e clicar no enter para passar para a próxima
nome=input('Nome: ')
idade=int(input('Idade: '))
altura=float(input('Altura em metro: '))
peso=float(input('Peso em kg: '))
imc=IMC(peso,altura)

#Segundo, através do print, irá exibir as expressões printadas + os valores das variáveis definidas anteriormente
exibe(nome,idade,altura,peso,imc)






