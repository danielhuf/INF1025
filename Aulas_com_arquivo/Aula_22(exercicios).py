#1 1. Faça um programa que percorre uma lista com o seguinte formato: [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. 
#O programa deve imprimir na tela: 
#a)	o total de faltas do campeonato 
#b)	o time que fez mais faltas 
#c)	o time que fez menos faltas
#Para os itens (b) e (c), você deve construir primeiro uma nova lista composta por sublistas com 2 elementos: [nome do país, total de faltas]

def busca(valor,lista):
    for (pos,el) in enumerate(lista):
        if el[0]==valor:
            return pos
    return None
    
l_campeonato=[['Brasil','Italia',[10,9]],['Brasil','Espanha',[5,7]],['Italia','Espanha',[7,8]]]
total_faltas=0
for el in l_campeonato:
    falta=el[2][0]+el[2][1]
    total_faltas+=falta
print('Total de faltas do campeonato = %d'%total_faltas)

l_Faltas=[]
for jogo in l_campeonato:
    for i in range(2):
        pos=busca(jogo[i],l_Faltas)
        if pos==None:
            l_Faltas.append([jogo[i],jogo[2][i]])
        else:
            l_Faltas[pos][1]+=jogo[2][i]

maisfaltas=l_Faltas[0][1]
menosfaltas=l_Faltas[0][1]
time_mais=l_Faltas[0][0]
time_menos=l_Faltas[0][0]
for el in l_Faltas[1:]:    #nao preciso perguntar para o primeiro
    if el[1]>maisfaltas:
        maisfaltas=el[1]
        time_mais=el[0]
    elif el[1]<menosfaltas:
        menosfaltas=el[1]
        time_menos=el[0]

print('Time com mais faltas',time_mais)
print('Time com menos faltas',time_menos)

#2 Questão única
#Uma instituição oferece cursos  em 3 turnos: M Manhã, T Tarde, N Noite e os alunos inscritos em disciplinas EaD, comuns aos cursos,  devem fazer a prova presencial, realizada em julho,   no turno de seu curso. O comitê de organização da prova e alocação das salas de aulas, precisa saber quantos alunos realizarão as provas em cada um dos turnos.
#O arquivo disciplinas.txt  armazena a quantidade de alunos nas diferentes disciplinas EaD, do seguinte modo:
#•	Disciplina (string);
#•	Qt de alunos inscritos na disciplina em cada um dos 3 turnos (3 inteiros)
#Exemplo do arquivo disciplinas.txt:
#LPO001
#400 200 1000		Significado  a disciplina LPO001 tem 400 alunos inscritos no turno manhã, 200 alunos inscritos no turno tarde e 1000 alunos inscritos no turno noite.

#No início do mês de junho, os alunos inscritos em alguma disciplina EaD podem solicitar a troca do turno para a realização da prova.  O arquivo texto solicitacoes.txt armazena, em pares de linhas, a disciplina, a matrícula do aluno, o turno origem e o turno destino:
#•	Disciplina (string);
#•	Matrícula do aluno (inteiro) turno de origem (M ou T ou N) turno destino (M ou T ou N) 
#Exemplo do arquivo solicitacoes.txt:
#LPO001
#102030 M T		Significado O aluno de matrícula 102030, matriculado no turno Manhã, deseja realizar a prova de LPO001 no turno Tarde.
		
#Faça um programa MODULARIZADO que, utilizando as informações armazenadas nos 2 arquivos, gere o arquivo ATUAL.TXT com a  quantidade de alunos que devem realizar as provas em cada um dos turnos  em cada um das  disciplinas. 
#Obrigatoriamente, o seu programa deve utilizar as seguintes funções feitas por você:
#a)	função busca(): implementa o algoritmo de busca sequencial;
#b)	função le_arq_disciplinas(): realiza a leitura dos dados do arquivo disciplinas.txts;
#c)	função atualiza_situacao: uma de suas responsabilidades é fazer a leitura dos dados do arquivo solicitacoes.txt, efetivando as operações realizadas;
#d)	função gera_arq_atual(): cria o arquivo ATUAL.TXT com as informações atualizadas;
#e)	função descobre_pos_turnos(): a função recebe o caractere que representa turno origem e o caractere que representa o  turno destino e retorna uma lista com o número do turno origem e o número do turno destino: 0 se for manhã, 1 se for tarde e 2 se for noite.  


def busca(valor,lista):
    for (pos,el) in enumerate(lista):
        if el[0]==valor:
            return pos
    return None

def le_arq_disciplinas():
    l=list()
    arq=open('disciplinas.txt','r')
    for disc in arq:
        nome=disc.strip()   #pega o nome da disciplina
        quantidade=arq.readline()
        l_quant=quantidade.split() #torna lista com os numeros
        for(pos,el) in enumerate(l_quant):
            l_quant[pos]=int(el)  #torna os numeros em inteiros
        l.append([nome,l_quant])
    arq.close()
    return l

def descobre_pos_turnos(O,D):
    l=list()
    lista=['M','T','N']
    l.append(lista.index(O))
    l.append(lista.index(D))
    return l

def atualiza_situacao(l_disc):
    arq=open('solicitacoes.txt','r')
    for disc in arq:
        nome=disc.strip()
        solic=arq.readline()
        l_solic=solic.split()  #cria lista com a matricula e os turnos
        turnoO=l_solic[1]   #turno de origem
        turnoD=l_solic[2]   #turno de destino
        pos=busca(nome,l_disc)
        l_pos=descobre_pos_turnos(turnoO,turnoD)
        posO=l_pos[0]
        posD=l_pos[1]
        if pos!=None:
            l_disc[pos][1][posO]-=1
            l_disc[pos][1][posD]+=1
    arq.close()
    return

def gera_arq_atual(l_disc):
    arq=open('atual.txt','w')
    for disc in l_disc:
        arq.write('%20s'%disc[0])
        for quant in disc[1]:
            arq.write('%10d'%quant)
        arq.write('\n')
    arq.close()

l_disc=le_arq_disciplinas()
atualiza_situacao(l_disc)
gera_arq_atual(l_disc)


    

            


    
