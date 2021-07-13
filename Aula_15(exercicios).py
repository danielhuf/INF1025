#1	Faça uma função que receba dois números (entre 10 e 99) e exiba na tela todos os números (inteiros e positivos) tais que:
#	Não terminem em zero;
#	Se o dígito da direita for removido, o número restante é divisor do número original.
#Exemplos:
#39: 3 é divisor de 39
#48: 4 é divisor de 48

def exibePositivo(n1,n2):
    if n1>n2:     #isso serve para inverter os valores e dar no mesmo, caso n1 seja maior que n2
        t=n1
        n1=n2
        n2=t
        n2=t
    cont=n1
    while cont<n2:
        if cont%10!=0:
            d=cont//10
            if cont%d==0:
                print('%d é divisor de %d'%(d,cont))
        cont+=1
    return

exibePositivo(10,99)

#2	Para realizar um debate sobre acesso a dados considerados sigilosos em campanhas políticas, um professor de ética resolveu agrupar seus 400 alunos em 3 grupos: o grupo “pró”, o grupo “contra” e o grupo “neutro”. Para saber a qual grupo o aluno pertence, o professor aplicou um questionário cujas respostas podem ser sim ou não.
#Faça uma função que recebe o número de questões, captura as respostas de cada uma das questões de um aluno e retorna a quantidade de respostas positivas.
#Obs: o aluno digita 's', quando concorda e 'n' quando discorda da questão
#Faça um programa que inicialmente capture o número de respostas do questionário. A seguir, para cada aluno da turma, obtenha sua matrícula e respostas (utilizando a função do item a), e exiba o nome de seu grupo de acordo com o seguinte critério:
#•	2/3 de respostas sim 	 grupo “pró”
#•	2/3 de respostas não 	 grupo “contra”
#•	Demais situações	 grupo “neutro”
# Obs.: Faça uma função para exibir o grupo de respostas. Esta função recebe o número de questões e a   quantidade de respostas SIM

def positivas(n):
    jafiz=0
    contpositiva=0
    while jafiz<n:
        quest=input('Sua respostas para essa questao?')
        if quest=='s':
            contpositiva+=1
        jafiz+=1
    return contpositiva

def exibe(ntotal,qtSim):
    razao=qtSim/ntotal
    if razao>2/3:
        print('pró')
    elif razao<1/3:
        print('contra')
    else:
        print('neutro')
    return

respostas=int(input('Numero de respostas do questionario:'))
cont=0
while cont<4:    #se der certo para 4, dara certo para 400
    mat=int(input('Matricula?'))
    t=positivas(respostas)
    print('%d é d grupo '%mat,end='')
    exibe(respostas,t)
    cont+=1
        
        
