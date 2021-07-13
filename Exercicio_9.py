#1 PODERIA TER SEPARADO TUDO EM DIFERENTES FUNÇÕES

def retornaTudo(lista):
    maiorElemento=lista[0]
    soma=0
    ocorrenciaPrimeiro=0
    somaNegativo=0
    vizinhosIguais=0
    for el in lista:
        if el>maiorElemento:
            maiorElemento=el
        soma+=el
        if el==lista[0]:
            ocorrenciaPrimeiro+=1
        if el<0:
            somaNegativo+=el
    pos=0
    while pos<len(lista)-1:
        if lista[pos]==lista[pos+1]:
            vizinhosIguais+=1
        pos+=1
    media=soma/len(lista)
    menorDistanciaMedia=abs(lista[0]-media)
    maisProximoMedia=lista[0]
    for el in lista:
        if abs(el-media)<menorDistanciaMedia:
            menorDisanciaMedia=abs(el-media)
            maisProximoMedia=el
    realOcorrenciaPrimeiro=ocorrenciaPrimeiro  
    return maiorElemento, soma, realOcorrenciaPrimeiro, media, maisProximoMedia, somaNegativo, vizinhosIguais

l=[30,30,20,900,30,-12,30,-14,20,0,0]
a=retornaTudo(l)
print(a)

#2
def maiorElemento(lista):
    for el in lista:
        if type(el)is int or type(el) is float:
            maiorEl=el
        elif type(el) is list:
            for i in el:
                if type(i) is int or type(i) is float:
                    maiorEl=i
    for el in lista:
        if type(el) is int or type(el) is float:
            if el>maiorEl:
                maiorEl=el
        elif type(el) is list:
            for i in el:
                if type(i) is int or type(i) is float:
                    if i>maiorEl:
                        maiorEl=i
    return maiorEl

def somaElementos(lista):
    soma=0
    for el in lista:
        if type(el) is int or type(el) is float:
            soma+=el
        elif type(el) is list:
            s=somaElementos(el)
            soma+=s
    return soma

def ocorrePrimeiro(lista):
    ocorrenciaPrimeiro=0  
    for el in lista:
        if el==lista[0]:
            ocorrenciaPrimeiro+=1
    return ocorrenciaPrimeiro

def mediaParcial(lista):
    n_numeros=0
    for el in lista:
        if type(el) is int or type(el) is float:
            n_numeros+=1
        elif type(el) is list:
            m=mediaParicial(el)
            n_numeros+=m
    return n_numeros

def mediaReal(lista):
    soma=somaElementos(lista)
    num=mediaParcial(lista)
    media=soma/num
    return media

def valorProximo(lista):
    med=mediaReal(lista)
    for el in lista:
        if type(el) is int or type(el) is float:
            val_mais_proximo=abs(el-med)
            item=el
        elif type(el) is list:
            for i in el:
                if type(i) is int or type(i) is float:
                    val_mais_proximo=abs(i-med)
                    item=i
    for el in lista:
        if type(el) is int or type(el) is float:
            if abs(el-med)<val_mais_proximo:
                val_mais_proximo=abs(el-med)
                item=el
        elif type(el) is list:
            for i in el:
                if type(i) is int or type(i) is float:
                    if abs(i-med)<val_mais_proximo:
                        val_mais_proximi=abs(i-med)
                        item=i
    return item

def somaNegativos(lista):
    soma=0
    for el in lista:
        if type(el) is int or type(el) is float:
            if el<0:
                soma+=el
        elif type(el) is list:
            s=somaNegativos(el)
            soma+=s
    return soma

def vizinhosIguais(lista):
    viz=0
    pos=0
    while pos<len(lista)-1:
        if lista[pos]==lista[pos+1]:
            viz+=1
        pos+=1
    return viz

print(maiorElemento(['oi',2,50,['ei',1000],200,[2,40]]))

#3
def iguais(l1,l2):
    if len(l1)==len(l2):
        pos=0
        while pos<len(l1):
            if l1[pos]==l2[pos]:
                a=True
            else:
                return False
            pos+=1
        return a
    return False

print(iguais([1,2],[1,3]))

def elIguais(l1,l2):
    l1_itens=[]
    l2_itens=[]
    for el in l1:
        if type(el)!=list:
            l1_itens.append(el)
        else:
            for i in el:
                l1_itens.append(i)
    for el in l2:
        if type(el)!=list:
            l2_itens.append(el)
        else:
            for i in el:
                l2_itens.append(i)
    if len(l1_itens)==len(l2_itens):
        for el in l1_itens:
            if el in l2_itens:
                a=True
            else:
                return False
        for el in l2_itens:
            if el in l1_itens:
                a=True
            else:
                return False
        return a
    return False

la=[1,'oi',2,'ei']
lo=['oi','ei',[2,1]]
print(elIguais(la,lo))

#4
def maisCaracter(lista):
    maior_item=lista[0]
    mais_car=len(lista[0])
    for el in lista:
        if len(el)>mais_car:
            maior_item=el
            mais_car=len(el)
    return maior_item

def mediaVogal(lista):
    n_itens=len(lista)
    soma_vogais=0
    for el in lista:
        for i in el:
            if i in 'aeiouAEIOU':
                soma_vogais+=1
    media=soma_vogais/n_itens
    return media

def ocorrenciaPrimeiro(lista):
    ocorre=0
    for el in lista:
        if el==lista[0]:
            ocorre+=1
    return ocorre

def maiorPalavra(lista):
    maiorPalavra=-1
    palavra=''
    for el in lista:
        s=el.split()
            for p in s:
                if len(p)>maiorPalavra:
                    maiorPalavra=len(p)
                    palavra=p
    return palavra

def numCompostas(lista):
    num=0
    for el in lista:
        if '-' in el:
            num+=1
    return num

def vizIguais(lista):
    viz=0
    pos=0
    while pos<len(lista)-1:
        if lista[pos]==lista[pos+1]:
            viz+=1
        pos+=1
    return viz

l=['oba','oioioioooooioioioioio','ai-o','oba','oba','oba','aaaaaaaaaaa','porta-perfume','ye','ye']
print(maiorPalavra(l))

#5
def maisCaracter(lista):
    maior_item=[]
    mais_car=-1
    for el in lista:
        if type(el) is str:
            if len(el)>mais_car:
                maior_item=el
                mais_car=len(el)
        else:
            for i in el:
                if len(i)>mais_car:
                    maior_item=i
                    mais_car=len(i)
    return maior_item

def mediaVogal(lista):
    n_itens=0
    soma_vogais=0
    for el in lista:
        if type(el) is str:
            for i in el:
                if i in 'aeiouAEIOU':
                    soma_vogais+=1
            n_itens+=1
        else:
            for palavra in el:
                for i in palavra:
                    if i in 'aeiouAEIOU':
                        soma_vogais+=1
                n_itens+=1
    media=soma_vogais/n_itens
    return media

def ocorrenciaPrimeiro(lista):
    ocorre=0
    for el in lista:
        if el==lista[0]:
            ocorre+=1
    return ocorre

def maiorPalavra(lista):
    maiorPalavra=-1
    palavra=''
    for el in lista:
        if type(el) is str:
            s=el.split()
                for p in s:
                    if len(p)>maiorPalavra:
                        maiorPalavra=len(p)
                        palavra=p
        else:
            for string in el:
                s=string.split()
                for p in s:
                    if len(p)>maiorPalavra:
                        maiorPalavra=len(p)
                        palavra=p
    return palavra

def numCompostas(lista):
    num=0
    for el in lista:
        if type(el) is str:
            if '-' in el:
                num+=1
        else:
            n=numCompostas(el)
            num+=n
    return num

def vizIguais(lista):
    viz=0
    pos=0
    pos_sublista=0
    while pos<len(lista)-1:
        if lista[pos]==lista[pos+1]:
            viz+=1
        pos+=1
    for el in lista:
        if type(el) is list:
            while pos_sublista<len(el)-1:
                if el[pos_sublista]==el[pos_sublista+1]:
                    viz+=1
                pos_sublista+=1
    return viz

l=[['oau','oau'],['oi','oau'],['oi','oau'],'ob-a','ob-a',['kkkkkkkkkk','alo']]
print(vizIguais(l))

#6
def traduzir(lSecreta):
    string=' abcdefghijklmnopqrstuvwxyz'
    decod=''
    for el in lSecreta:
        decod+=string[el]
    return decod

l=[2,15,13,0,4,9,1]
t=traduzir(l)
print(t)

#7 JÁ FOI FEITO NA AULA 22

#8
lista=[2.5,7.5,10.0,4.0]
soma=0
for el in lista:
    soma+=el
media=soma/len(lista)
item_prox=lista[0]
val_prox=abs(lista[0]-media)
for el in lista:
    if abs(el-media)<val_prox:
        val_prox=abs(el-media)
        item_prox=el
print('Valor mais próximo da média =',item_prox)

#9 JÁ FOI FEITO NA LISTA PARA O TESTE NUMERO 5

#10 JÁ FOI FEITO NA AULA 20

#11 
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

print(ordem([1,[5,4],2,3]))

#12
def ocorrencia(lNumeros,valor):
    if lNumeros==[]:
        return -2
    elif valor not in lNumeros:
        return -1
    else:
        pos=lNumeros.index(valor)
        return pos

def ocorrenciaComplexa(lNumeros,valor):
    if lNumeros==[]:
        return -2
    for (pos,el) in enumerate(lNumeros):
        if type(el) is not list:
            if valor==el:
                return pos
        else:
            for (p,i) in enumerate(el):
                if i==valor:
                    return str(pos)+'['+str(p)+']'
    return -1

l=[1,2,[5,7],5]
print(ocorrenciaComplexa(l,5))

#13
def uniao(l1,l2):
    for el in l2:
        if el not in l1:
            l1.append(el)
    return l1

def intersecao(l1,l2):
    l_inter=[]
    for el in l1:
        if el in l2:
            l_inter.append(el)
    return l_inter

def intercala(l1,l2):
    if len(l1)>=len(l2):
        maior=l1
        menor=l2
    else:
        maior=l2
        menor=l1
    l_intercala=[]
    pos=0
    for el in menor:
        l_intercala.append(l1[pos])
        l_intercala.append(l2[pos])
        pos+=1
    resto_maior=maior[pos:]
    for el in resto_maior:
        l_intercala.append(el)
    return l_intercala

la=[1,2,'i']
lo=[44,2.9,1,2,'ao']
print(intercala(la,lo))

#14
def megasena(result,l_jogo):
    l_venc=[]
    for el in l_jogo:
        if el[1]==result:
            l_venc.append(el[0])
    return l_venc

apostas=[[111,[1,2,90,40]],[202,[2,29,9,0]],[292,[28,2,39,93]]]
r=[28,2,39,93]
print(megasena(r,apostas))

#15
def recalcula(l_notas):
    maior=l_notas[0]
    l_novo=[]
    for el in l_notas:
        if el>maior:
            maior=el
    for (pos,el) in enumerate(l_notas):
        nova=el*10/maior
        print('%d   %.1f   %.1f'%(pos+1,el,nova))
    return

l=[3.0,4.0,5.0,6.0,3.0]
recalcula(l)

#16
def busca(valor,lista):
    for (pos,el) in enumerate(lista):
        if el[0]==valor:
            return pos
    return None

def exibeDados(l_cursos,l_aprov):
    for el in l_aprov:
        pos=busca(el[1],l_cursos)
        vagas_curso=l_cursos[pos][2]
        if el[2]<=(1/4)*vagas_curso:
            horario='8h às 11:30h'
        elif el[2]<=(2/4)*vagas_curso:
            horario='12h às 11:30h'
        elif el[2]<=(3/4)*vagas_curso:
            horario='14h às 15:30'
        else:
            horario='16h às 17:30'
        print('%10s   %10s   %s   %s'%(el[0],el[1],l_cursos[pos][1],horario))
    return

cursos=[['Engenharia','12/07',4],['Direito','10/12',4]]
ap=[['Lau','Direito',4],['Dan','Engenharia',1],['Pou','Direito',2],['Luis','Direito',1],['Ilana','Engenharia',4],['Flavio','Direito',3],['Leo','Engenharia',2],['Armando','Engenharia',3]]
exibeDados(cursos,ap)

#17 JÁ FOI FEITO NA LISTA PARA O TESTE NUMERO 5

#18 JÁ FOI FEITO NA LISTA PARA O TESTE NUMERO 5

#19
l_jogo=[['cachorro','dog'],['oi','hello'],['professor','teacher'],['pai','father'],['mãe','mother'],['ciência','science'],['casa','house'],['caneta','pen'],['escola','school'],['religião','religion']]
usados=[]
resumo_jogo=[]
rodada=1
pontos=0

while rodada<=5:
    print('RODADA',rodada)
    pos=int(input('Posição da palavra desejada: '))
    pos=pos-1
    while pos in usados:
        print('Palavra já foi utilizada. Por favor, escolha outra palavra.')
        pos=int(input('Posição da palavra desejada: '))
        pos=pos-1
    usados.append(pos)
    idioma=input('Idioma a ser exibido: ')
    if idioma=='I':
        id_escolhido=1
        trad=0
    else:
        id_escolhido=0
        trad=1
    print('Palavra no idioma escolhido: %s'%l_jogo[pos][id_escolhido])
    traducao=input('Tradução? ')
    if traducao==l_jogo[pos][trad]:
        print('ACERTOU!')
        var='- Acertou a tradução'
        pontos+=1
    else:
        print('ERROU!')
        var='- Errou a tradução'
        pontos-=1
    resumo_jogo.append([rodada,l_jogo[pos][0],l_jogo[pos][1],var])
    rodada+=1

print('PONTUAÇÃO TOTAL =',pontos)
print('RESUMO DO JOGO')
for (pos,el) in enumerate(resumo_jogo):
    print('rodada',resumo_jogo[pos][0],'- palavra em português:',resumo_jogo[pos][1],'- palavra em inglês:',resumo_jogo[pos][2],resumo_jogo[pos][3])

#20 QUESTÃO MAL FORMULADA
import math

def CalculaCiclo(num_dias_entre,num_dias_ciclo):
    a=math.sin(math.radians(2*math.pi*num_dias_entre*num_dias_cico))
    return a

def MostraCicloseMensagem(ciclo1,ciclo2,ciclo3):
    1cic=ciclo1*100
    print('Valor do ciclo 1 =',1cic)
    2cic=ciclo2*100
    print('Valor do ciclo 2 =',2cic)
    3cic=ciclo3*100
    print('Valor do ciclo 3 =',3cic)
    if 1cic<=0 or 2cic<=0 or 3cic<=0:
        print('ALERTA! Existem ciclos em fase crítica ou negativa')
    return

def converteJuliano(data):
    dia=int(data[:2])
    mes=int(data[3:5])
    ano=int(data[6:])
    if mes<3:
        ano=ano-1
        mes=mes+12
    A=ano//100
    B=A//4
    C=2-A+B
    D=int(365.25*(ano+4716))
    E=int(30.6001*(mes+1))
    juliano=D+E+dia+0.5+C-1524.5
    return juliano

def mostraCiclos(data_nas,lista):


DisciplinaeProvas=[122,['12/02/2019','2/06/2019','25/08/2019']]     

#21
def busca(valor,lista):
    for(pos,el) in enumerate(lista):
        if valor==el[0]:
            return pos
    return None

lIngr=[['Arroz',100,5.00],['Carne',100,16.00],['Batata Inglesa',250,3.50],['Cenoura',100,3.00],['Queijo Minas',150,12.00]]
lPratos=[['Muito Escondidinho',['Batata Inglesa',3],['Queijo Minas',1],['Cenoura',1]],['Pastelão de Vento',['Batata Inglesa',4],['Carne',1]]]
lConsumo=[['Muito Escondidinho',12],['Pastelão de Vento',30]]
l_preco_porc_ing=[]
l_mercado=[]

#primeiro, irei calcular o preço de cada porção dos ingredientes
for (pos,el) in enumerate(lIngr):
    custo_porc=((lIngr[pos][1])/1000)*lIngr[pos][2]
    l_preco_porc_ing.append([lIngr[pos][0],custo_porc])

maior_custo=-1
pratomaiscaro=''
for el in lPratos:
    nome_prato=el[0]
    custo=0
    for i in el[1:]:
        pos=busca(i[0],l_preco_porc_ing)
        custo+=i[1]*l_preco_porc_ing[pos][1]
    print('%s = R$%.2f'%(nome_prato,custo))
    if custo>maior_custo:
        maior_custo=custo
        pratomaiscaro=nome_prato
print('Prato mais caro:',pratomaiscaro)

#l_mercado é a lista com os produtos e o número de porções total
for el in lConsumo:
    pos=busca(el[0],lPratos)
    for i in lPratos[pos][1:]:
        produto=busca(i[0],l_mercado)
        if produto==None:
            l_mercado.append([i[0],i[1]*el[1]])
        else:
            l_mercado[produto][1]+=i[1]*el[1]

for el in l_mercado:
    pos=busca(el[0],lIngr)
    quant=lIngr[pos][1]*el[1]
    quant_kilo=quant/1000
    print('Quantidade de',el[0],'a ser comprada =',quant_kilo,'kg')
                
        
    


        
    

            






        
        
    


        
        
            
