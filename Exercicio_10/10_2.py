def busca(valor,lista):
    for (pos,el) in enumerate(lista):
        if el[0]==valor:
            return pos
    return None

def atualiza_vencedor(lista):
    maispontos=-1
    campea=0
    for (pos,el) in enumerate(lista):
        soma_o=0
        soma_p=0
        soma_b=0
        for i in el[1:]:
            if i=='o':
                soma_o+=1
            elif i=='p':
                soma_p+=1
            else:
                soma_b+=1
        total=5*soma_o+3*soma_p+1*soma_b
        if total>maispontos:
            maispontos=total
            campea=pos
    return campea

def gera_saida_arquivo(lista):
    arq=open('quadro.txt','w')
    p=atualiza_vencedor(lista)
    for (pos,el) in enumerate(lista):
        soma_o=0
        soma_p=0
        soma_b=0
        for i in el[1:]:
            if i=='o':
                soma_o+=1
            elif i=='p':
                soma_p+=1
            else:
                soma_b+=1
        total=5*soma_o+3*soma_p+1*soma_b
        arq.write('%30s   %d   %d   %d   %d \n'%(el[0],soma_o,soma_p,soma_b,total))
        if pos==p:
            total_camp=total
    arq.write('Escola Campea: %s com %d pontos'%(lista[p][0],total_camp))
    arq.close()
    return

arq=open('medalhas.txt','r')
lDados=[]
for linha in arq:
    l=linha.strip()
    lista=l.split(',')
    pos=busca(lista[0],lDados)
    if pos==None:
        lDados.append([lista[0],lista[2]])
    else:
        lDados[pos].append(lista[2])
arq.close()

gera_saida_arquivo(lDados)




