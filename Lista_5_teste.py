#1
def limite(lista,lim_i,lim_s):
    pos_inicio=0
    pos_final=0
    for (pos,el) in enumerate(lista):
        if el<lim_i:
            pos_inicio=pos+1
        elif el==lim_i:
            pos_inicio=pos
        if el<=lim_s:
            pos_final=pos
    if limite_superior<lista[0]:
        print(lista[none])
    elif pos_final==len(lista)-1:
        print(lista[pos_inicio:])
    else:
        print(lista[pos_inicio:pos_final+1])
    return

lista_inicial=[12,14,15,16,18,20,24,26,28,32,34,38]
limite_inferior=13
limite_superior=26
limite(lista_inicial,limite_inferior,limite_superior)

#2
def exibeInverso(lista):
    print(lista[(len(lista)//2):]+lista[:len(lista)//2])
    return

l=[1,2,3,4,5]
exibeInverso(l)

#3
def MediaTurma(lista):
    soma_alturas=0
    alunos=len(lista)
    for el in lista:
        soma_alturas+=el[1]
    media_altura=soma_alturas/alunos
    return media_altura

def Conta_Baixinhos(lista,media):
    alunos_mais13_abaixo=0
    for el in lista:
        if el[0]>13 and el[1]<media:
            alunos_mais13_abaixo+=1
    return alunos_mais13_abaixo

def exibeAlunos(l):
    media_alt=MediaTurma(l)
    n=Conta_Baixinhos(l,media_alt)
    print('%d aluno(s) com mais de 13 anos possuem altura inferior à media de altura da turma.'%n)
    return

lista_alunos=[[12,1.7],[17,1.3],[14,1.25],[12,1.36],[11,1.5]]
exibeAlunos(lista_alunos)
    


