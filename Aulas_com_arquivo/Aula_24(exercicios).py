#1
##Elabore um programa para ler o arquivo notas.txt, que contém, em cada linha, o nome de um aluno e as notas que ele obteve nas provas P1, P2 e P3. Os dados presentes em uma linha estão separados por uma vírgula seguida de um espaço em branco.
##
##Você deve fazer executar os seguintes passos:
##
##•	Leia a linha que contém os dados de cada aluno e, para cada um, calcule a sua média ponderada (MP), por meio da seguinte equação: MP = (P1 + 2P2 + 3P3) / 6.
##•	Calcule a média aritmética da turma, calculada a partir das médias ponderadas de cada aluno. 
##•	Exiba os dados dos alunos (nome e notas) e as suas médias ponderadas. Cada linha deve conter os dados referentes a um único aluno. As notas e as médias devem ter apenas 1 casa decimal. Os campos devem ser exibidos com seus respectivos nomes.
##Exemplo:    Nome: joao, P1:1.0, P2:6.0, P3:10.0, MP:7.2
##•	Exiba uma mensagem contendo a média aritmética da turma, no formato média da turma: média encontrada. 
##•	Gere o arquivo mediasMaiores.txt, contendo apenas os dados dos alunos com média ponderada superior à média da turma. O arquivo deve conter, em cada linha, o nome de um aluno, as suas notas e a sua média ponderada. Os campos devem ser separados por vírgulas.
##•	Finalmente, exiba mensagem contendo o número de alunos com médias maiores do que a média da turma, no formato número de alunos com média maior do que a média da turma: número de alunos encontrado.
##
##Observações:
##
##Não se sabe quantos alunos tem a turma. As notas e a média, tanto exibidas como escritas no arquivo, devem ser números ponto flutuante (float) com 1 casa decimal. O arquivo de entrada só deve ser lido uma vez.
##Exemplo:
##Tendo como entrada o arquivo notas.txt, a saída do arquivo mediasMaiores.txt é:
##
##joao,  1.0,  6.0, 10.0,  7.2
##luiz,  3.0,  7.0,  9.0,  7.3
##ana,  2.0,  5.0,  9.0,  6.5
##
##E os dados exibidos pelo programa são:
##
##nome:jose, P1:  5.0, P2:  7.0, P3:  3.0, MP:  4.7
##nome:joao, P1:  1.0, P2:  6.0, P3: 10.0, MP:  7.2
##nome:luiz, P1:  3.0, P2:  7.0, P3:  9.0, MP:  7.3
##nome:ana, P1:  2.0, P2:  5.0, P3:  9.0, MP:  6.5
##nome:ada, P1:  5.0, P2:  5.0, P3:  5.0, MP:  5.0
##nome:rui, P1:  3.0, P2:  4.0, P3:  1.0, MP:  2.3
##nome:ivo, P1:  2.0, P2:  6.0, P3:  3.0, MP:  3.8
##media da turma =   5.3
##numero de alunos com media maior do que a media da turma: 3

arq=open('notes.txt','r')
n_alunos=0
somaMedias=0
n_acima=0
lDados=[]
for linha in arq:
    l=linha.strip()
    lista=l.split(', ')
    i=1
    while i<=3:
        lista[i]=float(lista[i])
        i+=1
    MP=(lista[1]+2*lista[2]+3*lista[3])/6
    lista.append(MP)
    lDados.append(lista)
    somaMedias+=MP
    n_alunos+=1
    print('Nome: %s, P1: %.1f, P2: %.1f, P3: %.1f, MP: %.1f'%(lista[0],lista[1],lista[2],lista[3],MP))
arq.close()

MediaTurma=somaMedias/n_alunos
print('Média da turma: %.1f'%MediaTurma)

arq=open('mediasMaiores.txt','w')
for el in lDados:
    if el[-1]>MediaTurma:
        arq.write('%s, %.1f, %.1f, %.1f, %.1f \n'%(el[0],el[1],el[2],el[3],el[4]))
        n_acima+=1  
arq.close()

print('Número de alunos com média maior que a média da turma:',n_acima)


