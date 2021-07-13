#1
#O arquivo consumidores.txt armazena, em cada linha, o nome completo (nome e sobrenome) e a idade de um consumidor de um tipo de biscoito. Esses dados estão separados por vírgula (‘,’).
#a)	Escreva uma função, chamada geraLista, que:
#•	Receba o nome desse arquivo (consumidores.txt);
#•	Retorne uma lista de listas, em que cada lista interna armazena um nome (apenas o nome, sem o sobrenome) e a quantidade de ocorrências desse nome no arquivo.
#b)	Escreva um programa para testar a função geraLista.
#Obs.: Caso a sua solução leia o arquivo mais de uma vez, o valor máximo desta questão será 2,0.

def busca(valor,lista):
    for (pos,el) in enumerate(lista):
        if el[0]==valor:
            return pos
    return None

def geraLista(nome):
    lista_completa=[]
    arq=open(nome,'r')
    for linha in arq:
        l=linha.strip()
        nome_idade=l.split(' ')
        pos=busca(nome_idade[0],lista_completa)
        if pos==None:
            lista_completa.append([nome_idade[0],1])
        else:
            lista_completa[pos][1]+=1
    arq.close()
    return lista_completa

a=geraLista('consumidores.txt')
print(a)

>>> 
>>> l=['rica math',12]
>>> l[0]=l[0].split()
>>> l
[['rica', 'math'], 12]
>>> l[0][0]
'rica'
>>> 

#2 Questão única
##Uma editora possui 5 distribuidoras (cujos códigos variam de 1 a 5) para os livros que publica. No arquivo LIVROS.TXT, para cada livro, estão armazenadas as seguintes informações: 
##	título do livro (string);
##	a quantidade em estoque do livro em cada distribuidora, em ordem crescente de código de distribuidora (valores inteiros).
##Exemplo do arquivo LIVROS.TXT:
##Eu Sei Que Vou Te Amar 
##10 0 82 12 54		Significado há 10 unidades na distribuidora 1, 0  na distribuidora 2, 82 na 3, 12  na 4 e 54 na 5 do livro “Eu Sei Que Vou Te Amar”
##O arquivo ATUALIZACOES.TXT armazena as seguintes informações por operação (venda ou reposição):
##	título do livro (string) 
##	código da distribuidora responsável pela operação (valor inteiro de 1 a 5); 
##	código da operação realizada (1 caractere: ‘v’ – venda, ‘r’ – reposição); 
##	quantidade de livros envolvida na operação (inteiro). 
##Exemplo do arquivo ATUALIZACOES.TXT:
##Eu Sei Que Vou Te Amar
##3 v 50		Significado   A distribuidora 3 realizou uma venda de 50 unidades do livro Eu Sei Que Vou Te Amar
##Observação: não há qualquer tipo de agrupamento/ordem neste arquivo e uma distribuidora pode realizar várias vendas e reposições do mesmo livro. 
##Faça um programa que, utilizando as informações armazenadas nos 2 arquivos, gere o arquivo FINAL.TXT com o título e a quantidade em estoque atualizada em cada uma das 5 distribuidoras para cada livro. Ao final, devem ser exibidos na tela, o código da distribuidora com a menor quantidade de livros e o título dos livros que estejam com estoque zerado em todas as distribuidoras
##Obrigatoriamente, o seu programa deve utilizar as seguintes funções (feitas por você):
##a)	le_arq_livros: realiza a leitura dos dados do arquivo livros.txt; 
##b)	atualiza_informacoes: realiza a leitura dos dados do arquivo ATUALIZACOES.TXT, atualizando os dados do estoque; operações com códigos inválidos e/ou títulos inexistentes devem ser ignoradas;
##c)	gera_relatorio_final: cria o arquivo FINAL.TXT com as informações atualizadas e exibe na tela as informações solicitadas: o título dos livros que estejam com estoque zerado em todas as distribuidoras e o código da distribuidora com a menor quantidade de livros em estoque; é a única função que imprime informações na tela; 


def busca(valor,lista):
    for (pos,el) in enumerate(lista):
        if el[0]==valor:
            return pos
    return None

def le_arq_livros():
    l_inicial=[]
    arq=open('livros.txt','r')
    for linha in arq:
        nome=linha.strip()
        l=arq.readline()
        l=l.split()
        for (pos,el) in enumerate(l):
            l[pos]=int(el)
        l_inicial.append([nome,l])
    arq.close()
    return l_inicial

def atualiza_informacoes(lista_inicial):
    arq=open('atualizacoes.txt','r')
    for linha in arq:
        l=linha.strip()
        pos=busca(l,lista_inicial)
        op=arq.readline()
        if pos!=None:
            op=op.strip()
            l_opera=op.split(' ')
            ed=int(l_opera[0])
            quant=int(l_opera[2])
            if l_opera[1]=='v':
                lista_inicial[pos][1][ed-1]-=quant
            elif l_opera[1]=='r':
                lista_inicial[pos][1][ed-1]+=quant
    arq.close()
    return lista_inicial

def gera_relatorio_final(lista_inicial):
    for el in lista_inicial:
        if el[1][0]+el[1][1]+el[1][2]+el[1][3]+el[1][4]<=0:
            print('Editora',el[0],'está com o estoque zerado')
    menor=0
    dist=1
    for el in lista_inicial:
        menor+=el[1][0]    #estabeleci um valor base para a primeira distribuidora
    for i in range(1,5):   #lera 5 vezes(as 5 editoras)
        soma=0
        for el in lista_inicial:
            soma+=el[1][i]
        if soma<menor:
            menor=soma
            dist=i
    print('Distribuidora',dist,'com a menor quantidade de livros em estoque')
    arq=open('final.txt','w')
    for el in lista_inicial:
        arq.write('%40s'%el[0])
        for quant in el[1]:
            arq.write('%10d'%quant)
        arq.write('\n')
    arq.close()
    return

l=le_arq_livros()
li=atualiza_informacoes(l)
gera_relatorio_final(li)
    
        
 
