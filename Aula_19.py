#join pega uma lista e transforma em string
#split separa uma lista a partir do valor que voce determina

#EXEMPLOS

list('O que acontece?')
['O', ' ', 'q', 'u', 'e', ' ', 'a', 'c', 'o', 'n', 't', 'e', 'c', 'e', '?']
mens='bom dia? Estamos bem'
lcar=list(mens)
lcar[0]='B'
lcar[4]='D'
lcar[-1]='!'
lcar
['B', 'o', 'm', ' ', 'D', 'i', 'a', '?', ' ', 'E', 's', 't', 'a', 'm', 'o', 's', ' ', 'b', 'e', '!']
mens1='#'.join(lcar)
mens1
'B#o#m# #D#i#a#?# #E#s#t#a#m#o#s# #b#e#!'
mens2=''.join(lcar)
mens2
'Bom Dia? Estamos be!'
lpal=mens.split()
print(lpal)
['bom', 'dia?', 'Estamos', 'bem']
lfr=mens.split('?')
print(lfr)
['bom dia', ' Estamos bem']
frase='oieeee'
print(frase.split())
['oieeee']

l1=[1,2,3]
print(3*l1)
print(l1[:1])

#substituir todos os q por 1

l=['q','q','q',2,3,'q','q','q']
l1=[1]*3
l[:3]=l1
l[5:]=l1
print(l)

lista=[-2,-1,0,1,2,3]
lista[:4]=[1]
print(lista)

def repete(s):
    listapal=s.split()
    tam=len(listapal)
    meio=tam//2
    listapal[meio]=(listapal[meio]+' ')*tam
    return ' '.join(listapal)

print(repete('quantas vezes a palavra será replicada?'))

#Estou criando uma lista de presença com varios nomes

nome=input('Nome do aluno: ')
l=[]

while nome!='fim':
    l+=[nome]
    nome=input('Nome do aluno: ')
for el in l:
    print('%-30s |_|_|_|_|_|'%el)   #essa é a maneira de formatar cada elemento com espaços certos
