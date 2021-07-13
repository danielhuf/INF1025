def busca(valor,lista):
    for (pos,el) in enumerate(lista):
        if el[0]==valor:
            return pos
    return None

def le_arq_equipes(lDados):
    arq=open('equipes.txt','r')
    for linha in arq:
        ano_cria=int(linha.strip())
        l=arq.readline()
        equipe=l.strip()
        lDados.append([equipe,ano_cria])
    arq.close()
    return lDados

def le_arq_tempos(lDados):
    arq=open('tempos.txt','r')
    for linha in arq:
        l=linha.strip()
        lista=l.split(',')
        nome_equipe=lista[1]
        pos=busca(nome_equipe,lDados)
        lTrechos=[]
        for el in lista[2:]:
            lTrechos.append(int(el))
        lDados[pos].append(lTrechos)
    arq.close()
    return lDados

def converte(valor):
    hora=valor//3600
    minutos=valor%3600
    minutos_real=minutos//60
    segundos=minutos%60
    h=str(hora)
    m=str(minutos_real)
    s=str(segundos)
    string=h+':'+m+':'+s
    return string

lDados=[]
l1=le_arq_equipes(lDados)
l2=le_arq_tempos(l1)


for el in l2:
    if len(el[2])<6:
        vezes=6-len(el[2])
        n=1
        while n<=vezes:
            el[2].append(9999)
            n+=1

rodada=1
while rodada<=6:
    pos=rodada-1
    campea=l2[0][0]
    menor_tempo=l2[0][2][pos]
    ano_cria=l2[0][1]
    for el in l2:
        if el[2][pos]<menor_tempo:
            campea=el[0]
            menor_tempo=el[2][pos]
            ano_cria=el[1]
        elif el[2][pos]==menor_tempo:
            if el[1]<ano_cria:
                campea=el[0]
                menor_tempo=el[2][pos]
                ano_cria=el[1]
    posicao=busca(campea,l2)
    tTotal=l2[posicao][2][0]+l2[posicao][2][1]+l2[posicao][2][2]+l2[posicao][2][3]+l2[posicao][2][4]+l2[posicao][2][5]
    tTotal_formato=converte(tTotal)
    print('Equipe campeã do trecho %d: %s'%(rodada,campea))
    print('Ano da criação: %d'%ano_cria)
    print('Tempo no trecho atual: %d   Tempo total da equipe: %s \n'%(menor_tempo,tTotal_formato))
    rodada+=1
    
        
        
        
