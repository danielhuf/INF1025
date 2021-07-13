#(D) para repetição determinada e (I) para indeterminada

#1
def altura(h_inicial,taxa,n):
    cont=0
    altura=h_inicial
    while cont<n:
        altura=altura+(taxa/100)*altura
        cont+=1
    return altura

print(altura(100,10,2))

#2  
vbasico=float(input('Valor inicial = '))
mes=1

while mes<=12:
    print('Valor no mês %d: R$%.2f'%(mes,vbasico))
    mes+=1
    vbasico+=(5/100)*vbasico

#3
def duplica(v_inicial,taxa):
    tx=1+taxa/100
    anos=0
    valor=v_inicial
    
    while valor<2*v_inicial:
        valor*=tx
        anos+=1

    return anos

print(duplica(100,10),'anos')

#4
def altura(h_Hugo,h_Luis):
    if h_Hugo>h_Luis:
        return -1
    else:
        cm1=int(input('Quantos cm Hugo cresceu no ano? '))
        cm2=int(input('Quantos cm Luis cresceu no ano? '))
        ano=1
        while h_Hugo<h_Luis and (cm1+cm2!=0):
            h_Hugo+=cm1
            h_Luis+=cm2
            ano+=1
            cm1=int(input('Quantos cm Hugo cresceu no ano? '))
            cm2=int(input('Quantos cm Luis cresceu no ano? '))
        return ano

print(altura(90,180))

#5 FIZ PARECIDO NA LISTA 3 PARA O TESTE

#6
n=0
maior_idade=0
menos_11=0
id_mais_velho=-1
mais_velho=''

nome=input('Nome da pessoa: ')
while nome!='':
    idade=int(input('Idade da pessoa: '))
    if idade>id_mais_velho:
        id_mais_velho=idade
        mais_velho=nome
    if idade>=18:
        maior_idade+=1
    else:
        if idade<11:
            menos_11+=1
    n+=1
    nome=input('Nome da pessoa: ')

if n>=5:
    if maior_idade>=n//2:
        if menos_11==0:
            print('O grupo pode participar da excursão')
            print('Nome do líder = %s'%mais_velho)
        else:
            print('O grupo não pode participar da excursão')
    else:
        print('O grupo não pode participar da excursão')
else:
    print('O grupo não pode participar da excursão')
        
#7 FIZ PARECIDO NA LISTA 3 PARA O TESTE

#8
def processames():
    n=int(input('Quantos meses? '))
    cont=0
    nbaixo=0

    while cont<n:
        mes=input('Mes escolhido? ')
        if mes=='dezembro' or mes=='janeiro' or mes=='fevereiro' or mes=='junho' or mes=='julho':
            print('mes de alta temporada')
        else:
            print('mes de baixa temporada')
            nbaixo+=1
        cont+=1

    print('%.d mes(es) na baixa temporada'%nbaixo)
    return nbaixo

users=1
user_com_uma_baixa_ao_menos=0

while users<=4:
    print('USUÁRIO %.d'%users)
    a=processames()
    if a>=1:
       user_com_uma_baixa_ao_menos+=1 
    users+=1

print('Número de usuários que escolheram pelo menos um mes de baixa temporada = %.d'%user_com_uma_baixa_ao_menos)

#9
n=int(input('Número de conveniados na família? '))
cont=1

while cont<=n:
    ida=int(input('Idade do conveniado %.d? '%cont))
    if ida>60:
        adicional=130
    elif ida<10:
        adicional=80
    elif ida>=40:
        adicional=95
    else:
        adicional=50
    valor=100+adicional
    print('Valor a ser pago = RS%.2f'%valor)
    cont+=1

#10
def valor_unitario(quant,tipo):
    if quant>10000:
        unit=3.30
    elif quant<=1000:
        if tipo=='R':
            unit=11.10
        else:
            unit=9.10
    elif quant>5000:
        unit=6.40
    else:
        unit=10.00
    return unit

n=int(input('Quantidade de clientes? '))
cont=1
valor_total=0
n_desconto=0

while cont<=n:
    q=int(input('Quantidade de perfume do cliente %.d? '%cont))
    t=input('Tipo de entrega (R para rápida e N para normal)? ')
    valor=q*valor_unitario(q,t)
    if t=='R' and valor>4000:
        valor=(70/100)*valor
        n_desconto+=1
    print('Valor total a pagar = US$%.2f'%valor)
    valor_total+=valor
    cont+=1

print('Valor total dos pedidos = US$%.2f'%valor_total)
print('Número de clientes que receberam desconto = %.d'%n_desconto)

#11

def media():
    n1=float(input('Nota 1: '))
    n2=float(input('Nota 2: '))
    n3=float(input('Nota 3: '))
    n4=float(input('Nota 4: '))
    n5=float(input('Nota 5: '))
    n6=float(input('Nota 6: '))
    media=(n1+n2+n3+n4+n5+n6)/6
    return media
    
n=int(input('Quantidade de candidatos do Rio de Janeiro do concurso: '))
cont=1
aprovados=0
reprovados=0
somanotas=0

while cont<=n:
    nome=input('Nome do candidato %d: '%cont)
    nota=media()
    if nota>80:
        print('Candidato aprovado')
        aprovados+=1
    else:
        print('Candidato reprovado')
        reprovados+=1
    somanotas+=nota
    cont+=1

print('%d aprovados no total'%aprovados)
print('%d reprovados no total'%reprovados)
if n>0:
    print('Nota média dos candidatos = %.1f'%(somanotas/n))

#12 ESTÁ DEMORANDO MUITO PARA RODAR

def soma_Divisores(n):
    num=1
    soma_divisores=0
    while num<n:
        if n%num==0:
            soma_divisores+=num
        num+=1
    return soma_divisores

def exibe_Amigaveis():
    n1=1
    while n1<100000:
        n2=n1+1
        while n2<100000:
            if n1==soma_Divisores(n2) and n2==soma_Divisores(n1):
                print(n1,'e',n2)
            n2+=1
        n1+=1
    return

exibe_Amigaveis()

#13
def cresceDiario():
    print('1 de outubro, pessoas que sabem = 3')
    dia=2
    sabem=3
    while dia<26:
        sabem=sabem+2**dia
        print('%d de outbro, pessoas que sabem = %d'%(dia,sabem))
        dia+=1
    if sabem>20000:
        print('Funcionário deve ser demitido')
    else:
        print('Funcionário não deve ser demitido')
    return

cresceDiario()

#14 JÁ FOI FEITO EM SALA DE AULA

#15
def defineprimo(n):
    if n==1:
        return False
    else:
        num=2
        while num<=n**(1/2):
            if n%num==0:
                return False
            num+=1
        return True

print(defineprimo(5))

#16
def exibeprimos(a,b):
    if a>=b:
        num=b
        limite=a
    else:
        num=a
        limite=b
    while num<=limite:
        if defineprimo(num):
            print(num)
        num+=1

exibeprimos(30,1)

#17
import random

def pertence(x,y):
    cont=y-5
    while cont<=y+5:
        if x==y:
            return True
        cont+=1
    return False

def exibe(x,y):
    if x==y:
        print('ok')
    elif pertence(x,y):
        print('***')
    else:
        print('~~~')
    return

diaG=random.randint(1,28)
mesG=random.randint(1,12)

exibe(15,diaG)
exibe(7,mesG)

#18

def totalComprado(n):
    prod=0
    v_total=0
    maiscaro=0
    while prod<n:
        preco=float(input('Preço do produto? '))
        if preco>maiscaro:
            maiscaro=preco
        v_total+=preco
        prod+=1
    print('Seu produto mais caro custou R$%.2f'%maiscaro)
    return v_total

mais200=0
n_clientes=0
v_geral=0
maior_cliente=''
maior_valor=0
cliente=input('Nome do cliente? ')

while cliente!='':
    cli=cliente
    quant=int(input('Quantidade de itens comprados? '))
    valor=totalComprado(quant)
    print('D - À vista em dinheiro ou cheque  = 1 x R$%.2f'%(0.80*valor))
    print('C - À vista com cartão de credito  = 1 x R$%.2f'%(0.75*valor))
    print('P - Parcelado no cartão  = 2 x R$%.2f'%(valor/2))
    print('J - Parcelado no cartão = 3 x R$%.2f'%((1.1*valor)/3))
    if valor>200:
        mais200+=1
    if valor>maior_valor:
        maior_valor=valor
        maior_cliente=cli
    n_clientes+=1
    v_geral+=valor
    cliente=input('Nome do cliente? ')

print('%d clientes compraram mais de R$200,00'%mais200)
if n_clientes>0:
    mediacompra=v_geral/n_clientes
    print('Valor médio por cliente = R$%.2f'%mediacompra)
print('Cliente com maior total comprado = %s'%cli)

#19
def bacteria(n):
    t=1
    novo=(0.3/100)*n
    while n<=2*n:
        if t%3==0:
            morre=(0.5/100)*novo
            n-=morre
        n+=novo
        novo=(0.3/100)*n
        t+=1
    return t

print(bacteria(100))

#20
def aplicacao(valor, taxa_i):
    mes=1
    valor_inicial=valor
    while valor<=2*valor_inicial:
        valor=((100+taxa_i)/100)*valor
        print('Mes %d - Taxa de Juros utilizada = %.2f%% - Montante Reajustado = R$%.2f'%(mes,taxa_i,valor))
        if valor%13==0:
            print('Um prêmio de R$1000,00 foi incorporado')
            valor+=1000
        if mes%12==0:
            taxa_i+=2
        elif mes%3==0:
            taxa_i+=0.2
        mes+=1
    print('O valor será duplicado em %d meses'%(mes-1))

aplicacao(1000,100)

#21
def combustivel(desG,desA,prec_gas,prec_alc,capacidade):
    quant_gas=capacidade
    while quant_gas>=0:
        quant_alc=capacidade-quant_gas
        valor=prec_gas*quant_gas+prec_alc*quant_alc
        autonomia=desG*quant_gas+desA*quant_alc
        print('Qt de Litros Gas = %.2f - Qt de Litros Alc = %.2f - Valor Gasto Tanque = R$%.2f - Autonomia = %.2f'%(quant_gas,quant_alc,valor,autonomia))
        quant_gas-=5
    return

combustivel(20.00,15.00,4.20,3.90,50)

#22
import random

def risk(valor,perc_acao,perc_cdi):
    RISCO=random.randint(0,10)
    return RISCO

def resultado(M,A,C,R):
    reajuste=M+M*(C/100)*(10-R)/100+M*(A/100)*R/100
    return reajuste

salario=float(input('Salario do Estagiario? '))
while salario>=0:
    apli_acao=100
    maior_apli=100
    menor_risco=11
    maior_ganho=-1

    while apli_acao>=0:
        apli_cdi=100-apli_acao
        risco=risk(salario,apli_acao,apli_cdi)
        retorno=resultado(salario,apli_acao,apli_cdi,risco)
        print('%d%% do salário em ações - %d%% do salário em cdi - risco %d - Resultado = R$%.2f'%(apli_acao,apli_cdi,risco,retorno))
        if risco<menor_risco:
            menor_risco=risco
            maior_ganho=retorno
            maior_apli=apli_acao
        elif risco==menor_risco and retorno>maior_ganho:
            maior_ganho=retorno
            maior_apli=apli_acao
        apli_acao-=10

    print('Para o menor risco observado, o percentual de ações que oferece o maior retorno é %d%%'%maior_apli)
    salario=float(input('Salario do Estagiario? '))

#23
v_geral=0
num_quarto=int(input('Número do quarto do hóspede: '))

while num_quarto!=0:
    num_dia=int(input('Número de diárias utilizadas pelo hóspede: '))
    consumo=float(input('Valor do consumo interno: '))
    andar_apto=num_quarto//100
    if andar_apto==1:
        val_dia=90
    elif andar_apto==2:
        val_dia=180
    elif andar_apto==3:
        val_dia=300
    else:
        val_dia=450
    v_total_dia=num_dia*val_dia
    subtotal=v_total_dia+consumo
    taxa=(10/100)*consumo+(6/100)*v_total_dia
    v_pagar=subtotal+taxa
    v_geral+=v_pagar
    print('Número do quarto %d'%num_quarto)
    print('%d diárias utilizadas'%num_dia)
    print('Valor unitário da diária = R$%.2f'%val_dia)
    print('Valor total das diárias = R$%.2f'%v_total_dia)
    print('Valor do consumo interno = R$%.2f'%consumo)
    print('Subtotal = R$%.2f'%subtotal)
    print('Taxa de Serviço = R$%.2f'%taxa)
    print('TOTAL GERAL = R$%.2f'%v_pagar)
    num_quarto=int(input('Número do quarto do hóspede: '))

print('Valor geral recebido = R$%.2f'%v_geral)

#24 JÁ FOI FEITO NO TESTE 2 DA G1

#25 JÁ FOI FEITO EM SALA DE AULA

#26
def iguais(s1,s2):
    pos1=0
    pos2=0
    string=''
    while s1[pos1]==s2[pos2]:
        string+=s1[pos1]
        pos1+=1
        pos2+=1
    return string

print(iguais('abacate','aberto'))

#27
def numpos(s,t):
    len_t=len(t)
    pos=0
    menorposicao=-1
    while pos<len(s):
        if t==s[pos:pos+len_t] and menorposicao==-1:   #fiz essa segurança para ele só pegar a primeira aparição, se ja tiver na segunda aparicao, menorposicao já será diferente de -1
            menorposicao=pos
        pos+=1
    if menorposicao!=-1:
        return menorposicao
    else:
        return False

print(numpos('biobanana','an'))

#28 ordem lexicografica = ordem alfabetica
def ordem(palavra):
    pos=0
    while pos<len(palavra):
        if pos==0:
            v=True
        elif palavra[pos]>=palavra[pos-1]:
            v=True
        else:
            v=False
        pos+=1
    return v

print(ordem('ano'))
print(ordem('bola'))

#29
def repetidos(s):
    pos=0
    verificado=''
    repetidas=''
    while pos<len(s):
        if s[pos] in verificado and s[pos] not in repetidas:
            print(s[pos])
            repetidas+=s[pos]
        verificado+=s[pos]
        pos+=1
    return

repetidos('banana')

#30
def naorepetidos(s):
    pos=0
    verificado=''
    while pos<len(s):
        if s[pos] not in s[pos+1:] and s[pos] not in verificado:   #nao pode estar nem a frente nem atras
            print(s[pos])
        verificado+=s[pos]
        pos+=1
    return

naorepetidos('anaconda')

#31
def inverte():
    nome=input('Nome do usuários (pode ser maiúsculo ou minúsculo): ')
    pos=-1
    n=1
    invertido=''
    while n<=len(nome):
        if 'A'<=nome[pos]<='Z':
            invertido+=nome[pos]
        elif 'a'<=nome[pos]<='z':
            maiusculo=chr(ord(nome[pos])-ord('a')+ord('A'))
            invertido+=maiusculo
        pos-=1
        n+=1
    print(invertido)
    return

inverte()

#32
string=input('Frase: ')
pos=0
cont_espaço=0
cont_a=0
cont_e=0
cont_i=0
cont_o=0
cont_u=0

while pos<len(string):
    if string[pos]==' ':
        cont_espaço+=1
    elif string[pos]=='a' or string[pos]=='A':
        cont_a+=1
    elif string[pos]=='e' or string[pos]=='E':
        cont_e+=1
    elif string[pos]=='i' or string[pos]=='I':
        cont_i+=1
    elif string[pos]=='o' or string[pos]=='O':
        cont_o+=1
    elif string[pos]=='u' or string[pos]=='U':
        cont_u+=1
    pos+=1

print('espaço %d vezes'%cont_espaço)
print('a %d vezes'%cont_a)
print('e %d vezes'%cont_e)
print('i %d vezes'%cont_i)
print('o %d vezes'%cont_o)
print('u %d vezes'%cont_u)

#33
string=input('Sequência de caracteres: ')
pos=0
sem_espaço=''
#RETIRAR TODOS OS ESPAÇOS DA SEQUENCIA
while pos<len(string):
    if string[pos]!=' ':
        sem_espaço+=string[pos]
    pos+=1

inicio=0
final=-1

tam=len(sem_espaço)
while inicio<(tam//2):
    if sem_espaço[inicio]==sem_espaço[final]:
        pal=True
    else:
        pal=False
    inicio+=1
    final-=1

if pal:
    print('%s é um palíndromo'%string)
else:
    print('%s não é um palíndromo'%string)

#34
def quadrado(n):
    impar=1
    cont=0
    quadrado=0
    if n==0:
        result=0
    else:
        while cont<abs(n):    #pode ser negativo ou positivo
            quadrado+=impar
            impar+=2
            cont+=1
        result=quadrado
    return result

print(quadrado(12))
print(quadrado(-8))

#35 NÃO SEI CALCULAR INTEGRAL

#36
def horario(hora):
    if '08:00'<=hora<='18:00':
        return True
    else:
        return False

def calculaMulta(vmax,vmot):
    ultrapasse=vmot-vmax
    if ultrapasse<=10:
        multa=50
    elif ultrapasse<=30:
        multa=100
    else:
        h=input('Hora em que ocorreu a multa: ')
        if horario(h):
            multa=200
        else:
            multa=400+2*(ultrapasse//1)
    return multa

maxima=int(input('Velocidade máxima permitida em km/h: '))
infratores=0
somamultas=0

v=int(input('Velocidade do infrator em km/h: '))
while v!=-1:
    m=calculaMulta(maxima,v)
    print('Multa recebida = R$%.2f'%m)
    infratores+=1
    somamultas+=m
    v=int(input('Velocidade do infrator em km/h: '))

if infratores>0:
    media=somamultas/infratores
    print('Valor médio das multas = R$%.2f'%media)

#37
def hora(hprev,hefet):
    if hprev==hefet:
        print('O voo chegou no horário')
    elif hprev<hefet:
        print('O voo chegou atrasado')
    else:
        print('O voo chegou adiantado')
    min_hprev=(int(hprev[:2]))*60+int(hprev[3:])
    min_hefet=(int(hefet[:2]))*60+int(hefet[3:])
    dif=min_hefet-min_hprev
    return dif

def voos_aeroporto(n):
    no_horario=0
    atrasados=0
    t_atrasos=0
    cont=0

    while cont<n:
        num=input('Código do voo? ')
        previsto=input('Horário previsto de chegada no formato hh:mm? ')
        efetivo=input('Horário efetivo de chegada no formato hh:mm? ')
        h=hora(previsto,efetivo)
        if h==0:
            no_horario+=1
        elif h>0:
            atrasados+=1
            t_atrasos+=h
        cont+=1

    print('%.2f%% de voos no horário'%(no_horario/n))
    if atrasados>0:
        print('Tempo médio de atraso = %.0f minutos'%(t_atrasos/atrasados))
    return atrasados

aero=1
mais_voos_atraso=-1
aeroporto_atraso=''
while aero<=10:
    nome=input('Nome do aeroporto: ')
    num=int(input('Numero de voos no dia: '))
    a=voos_aeroporto(num)
    print('Total de %d voos atrasados'%a)
    if a>mais_voos_atraso:
        mais_voos_atraso=a
        aeroporto_atraso=nome
    aero+=1

print('Maior número de voos em atraso no aeroporto %s'%aeroporto_atraso)

#38
def maior_18(idade):
    if idade>=18:
        return True
    else:
        return False

def determina_vale(ida,ntecnico,nnao):
    soma=ntecnico+nnao
    if not maior_18(ida) or soma<3:
        vale=0
    elif soma==3:
        if ntecnico==0 or nnao==0:
            vale=100
        else:
            vale=150
    else:
        vale=200
    return vale

cliente=0
while cliente<3:
    i=int(input('Idade do cliente: '))
    s=input('Sexo: ')
    t=int(input('Quantidade de livros tecnicos lidos em 2016: '))
    nt=int(input('Quantidade de livros nao tecnicos lidos em 2016: '))
    v=determina_vale(i,t,nt)
    print('Valor do vale = R$%.2f'%v)
    cliente+=1
    

    
            
        
        
        


    


        
    

    
    
    


    
        
