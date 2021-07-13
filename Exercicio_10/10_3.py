def busca(valor,lista):
    for (pos,el) in enumerate(lista):
        if el[0]==valor:
            return pos
    return None

def le_arq_contas():
    lDados=[]
    arq=open('contas.txt','r')
    for linha in arq:
        l=linha.strip()
        nome=l
        valores=arq.readline()
        val=valores.strip()
        l_valores=val.split(' ')
        lDados.append([nome,float(l_valores[0]),float(l_valores[1]),float(l_valores[2])])
    arq.close()
    return lDados

def atualiza_saldos(lista):
    arq=open('movimentacoes.txt','r')
    for linha in arq:
        l=linha.strip()
        pos=busca(l,lista)
        mov=arq.readline()
        transi=mov.strip()
        l_transi=transi.split(' ')
        if pos!=None:
            if l_transi[0]=='d':
                valor=float(l_transi[2])
                lista[pos][int(l_transi[1])]+=valor
            elif l_transi[0]=='r':
                valor=float(l_transi[2])
                lista[pos][int(l_transi[1])]-=valor
            else:
                lista[pos][int(l_transi[1])]=0.0
    arq.close()
    return lista

def gera_arquivo_atual(lista):
    arq=open('atual.txt','w')
    arq.write('RESULTADO ESPERADO \n \n')
    for el in lista:
        arq.write('%s \n'%el[0])
        arq.write('%.2f   %.2f   %.2f \n'%(el[1],el[2],el[3]))
    arq.close()
    return

lista1=le_arq_contas()
lista2=atualiza_saldos(lista1)
gera_arquivo_atual(lista2)


                
            
    
    

        
    
