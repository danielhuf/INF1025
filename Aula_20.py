#controlar inclusao e exclusao de novos alunos no curso
def incluiLista(lista,item):
    if item in lista:
        print('Já está matriculado')
    else:
        lista.append(item)
    return

def excluiLista(lista,item):
    if item not in lista:
        print('Não está matriculado')
    else:      #nao pode fazer -= em uma lista, já que nao existe operador -=
        pos=lista.index(item)    #index retorna a posicao do item na lista
        lista=lista[:pos]+lista[pos+1:]  #retirei atraves do slice
        #ou escreve lista.remove(m)
    return
    
l_alunos=[]

oper=input('Operação desejada? ')
while oper!='F':
    mat=int(input('Matrícula do aluno: '))
    curso=input('Curso do aluno: ')
    if 'Engenharia' not in curso:
        print('Só alunos de Engenharia podem se inscrever no curso')
    else:
        if oper=='I':
            incluiLista(l_alunos,mat)
        else:
            excluiLista(l_alunos,mat)
    oper=input('Operação desejada? ')

print('LISTA DE MATRICULADOS')
print(l_alunos)

#1
l_signos=['Macaco','Galo','Cão','Porco','Rato','Boi','Tigre','Coelho','Dragão','Serpente','Cavalo','Carneiro']
l_niver=['12/07/2002','24/12/1968','01/01/1947']

def exibeSigno(l1,l2):
    for el in l1:
        ano=el[6:]
        num=int(ano)%12
        print(l2[num])
    return

exibeSigno(l_niver,l_signos)

#2  lista e sublistas só de numeros
def ordem(l):
    tam=len(l)
    for i in range(tam-1):
        if type(l[i]) is list:
            r=ordem(l[i])
            if not r:
                return False
        else:
            if type(l[i+1]) is not list:
                if l[i]>l[i+1]:
                    return False
        return True

#3
l_nomes=[]
n=1
for i in range (6):
    nome=input('Nome')
    l_nomes.append(nome)

nam=input('Nome? ')
while nam!='fim':
    if nam in l_nomes:
        pos=l_nomes.index(nam)
        l_nomes[pos]=nam.upper()
    else:
        l_nomes.append(nam)
    print(l_nomes)
    nam=input('Nome: ')

#4
def contcaracter(lista):
    cont=0
    for i in lista:
        if type(i) is str:
            cont+=len(i)
        elif type(i) is list:
            s=contcaracter(i)
            cont+=s
    return cont

l=['oi','oi',2,['o i','i']]
print(contcaracter(l))

#5
def escolheHotel(lista):
    contf=0
    contm=0
    for i in lista:
        if i[1]=='f':
            contf+=1
        else:
            contm+=1
    if contf>contm:
        print('Pink Hotel')
    elif contm>contf:
        print('Hotel do Sport')
    else:
        print('Le Hotel')
    return

l=[['ana','f'],['pedro','m']]
escolheHotel(l)

#6
def criaLista(lista):
    L_escolas=[]
    L_nova=[]
    for el in lista:
        if el[1] not in L_escolas:
            L_escolas.append(el[1])
    for el in L_escolas:
        somapontos=0
        for i in lista:
            if i[1]==el:
                for a in i[2]:
                    if a=='o':
                        somapontos+=5
                    elif a=='p':
                        somapontos+=3
                    else:
                        somapontos+=1
        L_nova.append([el,somapontos])
    return L_nova

L_completa=[]

aluno=int(input('Aluno: '))
while aluno!=0:
    L_individual=[aluno]
    escola=input('Nome da escola: ')
    L_individual.append(escola)
    n=int(input('Quantas medalhas ganhou? '))
    m=0
    L_medalhas=[]
    while m<n:
        tipo=input('Tipo da medalha: ')
        L_medalhas.append(tipo)
        m+=1
    L_individual.append(L_medalhas)
    L_completa.append(L_individual)
    aluno=int(input('Aluno: '))

w=criaLista(L_completa)
campeã=''
pontos_campeã=0
for el in w:
    print('%d pontos totais para a escola %s'%(el[1],el[0]))
    if el[1]>pontos_campeã:
        pontos_campeã=el[1]
        campeã=el[0]
print('A escola campeã foi %s com um total de %d pontos'%(campeã,pontos_campeã))

#7
import random

def geraExibe(lista):
    especiais=['!','@','#','$','%']
    sub=1
    while sub<=30:
        num=random.randint(0,100)
        l1=random.randint(65,90)
        letra_1=chr(l1)
        l2=random.randint(65,90)
        letra_2=chr(l2)
        digi_1=str(random.randint(0,9))
        digi_2=str(random.randint(0,9))
        pos1=random.randint(0,4)
        caracter_1=especiais[pos1]
        pos2=random.randint(0,4)
        caracter_2=especiais[pos2]
        senha=letra_1+letra_2+digi_1+digi_2+caracter_1+caracter_2
        sublista=[num,senha]
        lista.append(sublista)
        sub+=1
    print(lista)
    return

def busca(listagerada,num):
    for (pos,el) in enumerate(listagerada):
        if el[0]==num:
            return pos
    return -1

l=[]
geraExibe(l)
numero=int(input('Solicite um numero de usuario: '))
b=busca(l,numero)
print('Primeira ocorrência na posição %s'%b)

#8
def avalia(lista,senha,intervalo,criterio):
    tam=len(senha)
    pos=0
    contem=False
    while pos<tam:
        if senha[pos] in intervalo:
            contem=True
        pos+=1
    if contem:
        lista.append(criterio)
    return


def classificaUmaSenha(s):
    L_criterios=[]
    avalia(L_criterios,s,'1234567890',1)
    avalia(L_criterios,s,'ABCDEFGHIJKLMNOPQRSTUVWXYZ',2)
    avalia(L_criterios,s,'!$@#%()',3)
    if 1 in L_criterios and 2 in L_criterios and 3 in L_criterios:
        nivel='FORTE'
    elif 1 in L_criterios:
        nivel='MEDIO'
    elif 2 in L_criterios:
        nivel='RAZOAVEL'
    elif 3 in L_criterios:
        nivel='FRACO'
    else:
        nivel='MUITO FRACO'
    return nivel

def classificaTodasSenhas(n):
    cont=1
    abaixo_medio=0
    while cont<=n:
        senha=input('Senha para o respectivo deposito: ')
        niv=classificaUmaSenha(senha)
        print('Nível de segurança da senha %s'%niv)
        if niv!='MEDIO' and niv!='FORTE':
            abaixo_medio+=1
        cont+=1
    return abaixo_medio

def determinaQtdDepositos(cat):
    if cat=='aluno':
        n=1
    elif cat=='professor' or cat=='pesquisador':
        n=2
    else:
        n=4
    return n

c=input('Categoria do usuario: ')
total_senhas=0
total_abaixo=0
while c!= 'FIM':
    num=determinaQtdDepositos(c)
    total_senhas+=num
    s=classificaTodasSenhas(num)
    total_abaixo+=s
    c=input('Categoria do usuario: ')
percent=(total_abaixo/total_senhas)*100
print('%.2f%% de senhas com nivel de segurança inferior ao nível de segurança medio'%percent)


    
    
    
    
    


        

        
    
    

    


