#ARQUIVOS
arq=open('arquivo_20.txt','r')
texto=arq.read()    #le o texto
print(texto)
arq.close()    #deve-se fechar o arquivo para executar a leitura ou escrita 

arq=open('arquivo_20.txt','r')    #isso so funciona se o arquivo estiver na mesma pasta do meu programa
for linha in arq:
    linha=linha.strip()      #retira os elementos em branco, no caso foi o enter para a proxima linha
    print(linha)
arq.close()

#Le esse arquivo e printa o nome dos estudantes com media maior que 5
def lista_aprovados(nome):
    arq=open(nome,'r')
    for linha in arq:
        L_linha=linha.strip().split(',')   #strip tira espaço e split cria a lista com itens entre virgulas
        nota1=float(L_linha[1])
        nota2=float(L_linha[2])
        media=(nota1+nota2)/2
        if media>=5.0:
            print(L_linha[0])
    arq.close()
    return

lista_aprovados('arquivo_20_2.txt')

#1	Faça um programa que leia um número “coringa” do teclado e um conjunto de valores inteiros positivos do arquivo números.txt.  Dentre os valores lidos, o programa deve guardar em outro arquivo os números que são múltiplos do “coringa”

coringa=int(input('Numero: '))
arq_s=open('coringa.txt','w')   #saida
arq_e=open('numeros.txt','r')   #entrada
for linha in arq_e:
    if int(linha)%coringa==0:
        arq_s.write(linha)   #devo escrever em formato de string
arq_s.close()
arq_e.close()

#2 Um professor salvou
#	no arquivo "p1.txt": a matrícula e o resultado da prova P1 de cada aluno de sua turma  
#	no arquivo "t1.txt": a matrícula e a nota do teste T1  de cada aluno de sua turma
#Os dois arquivos estão organizados por matrícula e contém em cada linha a matrícula e nota de seus alunos.  Todos os alunos compareceram nas duas avaliações.
#Faça um programa que monte e exiba uma lista onde cada elemento é composto por: 
#	[matrícula do aluno, média G1, [nota da P1, nota da T1]]
#A média da G1 é calculada por: (P1*0.8 + T1*0.2)
#No final seu programa deve armazenar no arquivo Preocupacoes.txt a matrícula e a média dos alunos que tiraram menos de 4 na prova P1 e mais do que 7 no teste T1 e no arquivo Notas.txt, a matrícula, a média, a nota P1 e a nota T1 de todos os alunos.

prova=open('p1.txt','r')
teste=open('t1.txt','r')
l=list()

for linhaP in prova:
    L_ap=linhaP.split()
    linhaT=teste.readline()   #todo readline vai lendo a proxima quando é repetido
    L_at=linhaT.split()
    matr=int(L_ap[0])
    p1=float(L_ap[1])
    t1=float(L_at[1])
    media=p1*0.8+t1*0.2
    l.append([matr,media,[p1,t1]])
prova.close()
teste.close()

print(l)
preo=open('Preocupacoes.txt','w')
nota=open('Notas.txt','w')
for aluno in l:
    nota.write('%d %.1f %.1f %.1f \n'%(aluno[0],aluno[1],aluno[2][0],aluno[2][1]))
    if aluno[2][0]<4 and aluno[2][1]>7:
        preo.write('%d %.1f \n'%(aluno[0],aluno[1]))
preo.close()
nota.close()
    

    
  
        
    
        
