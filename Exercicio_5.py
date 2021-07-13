#1
def aprovacao(alunos,aprovados):
    percent=(aprovados/alunos)*100
    print('Aprovados: %.1f%%'%percent)
    return

alun=int(input('Alunos: '))
aprov=int(input('Aprovados: '))
aprovacao(alun,aprov)

#2
t=60*60*float(input('Horas: '))
print(t*30,'km/s')

#3 FEITO NA LISTA 2 PARA O TESTE

#4 FEITO NA LISTA 2 PARA O TESTE

#5 FEITO NA LISTA 2 PARA O TESTE

#6 FEITO NA LISTA 2 PARA O TESTE

#7 FEITO NA LISTA DE EXERCICIOS DA AULA 11

#8
#a)b)
def lerTamanho(tamanho,velocidade):
    tempo=tamanho/velocidade   #será dado em segundos
    tempo_horas=tempo//3600
    tempo_minutos=(tempo%3600)//60
    tempo_segundos=(tempo%3600)%60
    print('Tempo aproximado em horas,minutos e segundos:',tempo_horas,':',tempo_minutos,':',tempo_segundos)
    return

arquivo=float(input('Tamanho de um arquivo para download (em Mb):'))
vel=float(input('Velocidade do link de internet (em Mb/s):'))

lerTamanho(arquivo,vel)

#9  FEITO, ACHO QUE NA PRIMEIRA AULA SOBRE ENTRADA E SAIDA

#10
def area_Mosteller(altura,peso):
    A=((peso*altura)**(1/2))/60
    return A

def area_Haycock(altura,peso):
    A=(peso**0.5378)*(altura**0.3964)*0.024265
    return A

def juntaFormulas(height,tall):
    areacorp1=area_Mosteller(height,tall)
    areacorp2=area_Haycock(height,tall)
    dif=areacorp1-areacorp2
    print('Área pela forma de Mosteller(m2): %.2f, Área pela forma de Haycock(m2): %.2f, Diferença(m2): %.2f'%(areacorp1,areacorp2,dif))
    return

alt=float(input('Altura em cm:'))
pes=float(input('Peso em kg:'))

juntaFormulas(alt,pes)

#11
def digitoVerif(num_conta):
    inverso=((str(num_conta))[-1])+((str(num_conta))[-2])+((str(num_conta))[-3])
    soma=num_conta+int(inverso)
    resultado=((soma//100)*1)+(int((str(soma))[1])*2)+((soma%10)*3)
    verificador=(str(resultado))[-1]
    verificador_num=int(verificador)
    return verificador_num

v=digitoVerif(256)

#12
def calculaValor(vi,i,t):
    vp=vi+vi*(i/100)*(t/100)
    return vp

taxa=int(input('Valor da taxa(%): '))
c=calculaValor(1000,taxa,2)

#13
def volumeKit(r,altura,quantidade):
    volume=quantidade*(3.14159*r*r*altura)
    custo=quantidade*10
    preco_venda=130/100*custo
    print('Volume: %.2f, Custo do kit (em reais): %.2f, Preço de venda (em reais): %.2f'%(volume,custo,preco_venda))
    return

quant=int(input('Quantidade de latas de um kit: '))
volumeKit(0.5,3,quant)

#14
def exibeDados(num_mat):
    matricula=str(num_mat)
    ano_ingresso='20'+matricula[:2]
    semestre=matricula[2]+'º semestre'
    print('Ano de ingresso:',ano_ingresso,'Semestre de ingresso:',semestre)
    return

num=input('Número de matrícula no formato AASDDD: ')
exibeDados(num)

#15
def tempoNecessario(dist,vel):
    tempo=dist/vel  #resultado em horas
    tempo_minutos=tempo*60
    horas=tempo_minutos//60
    minutos=tempo_minutos%60
    paradas=horas//1
    tempo_total_minutos=tempo_minutos+(paradas*15)
    horas_total=tempo_total_minutos//60
    minutos_total=tempo_total_minutos%60
    velocidade_hipot=dist/(tempo_total_minutos/60)
    print('Tempo necessário de viagem(total decorrido): %2.0fh:%2.0fmin Número de paradas:%d Velocidade hipotética sem paradas em km/h:%2.2f'%(horas_total,minutos_total,paradas,velocidade_hipot))
    return

distancia=float(input('Distância em km: '))
velocidade=float(input('Velicidade em km/h: '))
tempoNecessario(distancia,velocidade)

#16
def tempoPerdido(cig_dia,anos):
    total_cigarro=anos*360*cig_dia
    minutos_perdidos=total_cigarro*10
    horas_perdidas=minutos_perdidos/60
    dias_perdidos=horas_perdidas/24
    anos_perdidos=dias_perdidos/360
    anos=anos_perdidos//1
    meses=(anos_perdidos-anos)*12
    meses_final=meses//1
    dias=(meses-meses_final)*30
    print('Redução do tempo de vida: %d anos, %d meses e %.2f dias'%(anos,meses_final,dias))
    return

num_cig=int(input('Número de cigarros por dia: '))
num_anos=int(input('Número de anos fumando: '))
tempoPerdido(num_cig,num_anos)

#17
def pontuacao(vitoria,empate,derrota):
    p1=vitoria*3
    p2=empate*1
    p3=derrota*0
    total=p1+p2+p3
    print('Pontuação total:',total,'pontos')
    return

num_vit=int(input('Número de vitórias: '))
num_emp=int(input('Número de empates: '))
num_der=int(input('Número de derrotas: '))

pontuacao(num_vit,num_emp,num_der)

#18
def razao(arremessos,cestas):
    r=arremessos/cestas
    print('Razão = %.2f'%r)
    return

num_arr=int(input('Número de arremessos: '))
num_ces=int(input('Número de cestas: '))

razao(num_arr,num_ces)

#19 FEITO EM ALGUM MOMENTO

#20
def campanha(arroz_arrec,quant_fam):
    num_fam=int(arroz_arrec//quant_fam)
    print('Número de famílias atendidas:',num_fam)
    return

num_arroz=float(input('Quantidade de arroz arrecadada em kg: '))
num_fam=float(input('Quantidade de arroz para cada familia em kg: '))

campanha(num_arroz,num_fam)

#21
def quant_fam(quant_arrec,familias):
    recebido=quant_arrec//familias
    print('Kg de arroz por família:',recebido)
    return

arrecadado=float(input('Quantidade de arroz arrecadada em kg: '))
fam=int(input('Número de famílias atendidas: '))

quant_fam(arrecadado,fam)

#22
def trocaData(data):
    inverso=data[3:5]+'/'+data[:2]+'/'+data[6:]
    print(inverso)
    return

dat=input('Data no formato dd/mm/aaaa: ')

trocaData(dat)

#23
#a)b)
def inverso(string):
    inv=string[-1::-1]
    return inv

def geraString(nome,alg,n):
    alt=nome[:n]+inverso(alg)
    return alt

x=geraString('Patinhas','19',3)

#c)
def cadastro(nome,ano):
    login=nome+inverso((str(ano))[2:])
    senha=geraString(nome,str(ano),(len(nome)//2))
    print('Login:',login,'Senha:',senha)
    return

nom=input('Nome: ')
dat=int(input('Ano de nascimento: '))

cadastro(nom,dat)

#24
import random

def transmissao(nome,sobrenome,n):
    cod=nome[:n]+sobrenome[:n]+'*'+nome[n:]+'&'+sobrenome[n:]
    print('Dados transmitidos:',cod)
    return

nom=input('Nome: ')
sobre=input('Sobrenome: ')
rand=random.randint(1,abs(len(nom)-len(sobre)))

transmissao(nom,sobre,rand)

#25     ESTÁ DANDO ERRO
def concatena(s1,s2):
    print(s1[:len(s1)//2]+s2[(len(s2)//2)+((len(s2)%2)/(len(s2)%2)):])
    return 

mae=input('Nome da mãe: ')
pai=input('Nome do pai: ')

concatena(mae,pai)

#26
def valores(valor_compra,nparc):
    ventrada=(30/100)*valor_compra
    vparcela=((70/100)*valor_compra)/nparc
    taxa_adm=(10/100)*((70/100)*valor_compra)
    ventrada_com_taxa=ventrada+taxa_adm
    print('Valor de entrada = R$ %.2f Valor de cada parcela = R$ %.2f'%(ventrada_com_taxa,vparcela))
    return

vcomp=float(input('Valor de compra: '))
n=int(input('Numero de parcelas: '))

valores(vcomp,n)
          
#27 FEITA NA LISTA 2 PARA O TESTE

#28
def metragem(d1,d2):
    result=d1*d2
    return result

def exibemetragem(dim1,dim2):
    print('Metragem:',metragem(dim1,dim2),'metros quadrados')
    return

dimensao1=float(input('Largura do quadro em metro: '))
dimensao2=float(input('Comprimento do quadro em metro: '))

exibemetragem(dimensao1,dimensao2)

#29
def converte(medida):
    metro=medida//100
    centi=medida%100
    print(metro,'m',centi,'cm')
    return

altura=int(input('Altura em cm: '))

converte(altura)

#30
def conjuga(verbo):
    pret=verbo+'ia'
    print('Futuro do pretérito =',pret)
    return

verb=input('Verbo regular terminado em AR: ')

conjuga(verb)

#31
def gasolina(prec_EUA,taxa_conv):
    prec_BR=prec_EUA*taxa_conv    #preço do galao
    litro=prec_BR/3.7854
    print('Preço do litro de gasolina: R$%.2f'%litro)
    return

dolar=float(input('Preço em dólar do galão de gasolina dos EUA: '))
conv=float(input('Taxa de conversão do dólar para o real: '))

gasolina(dolar,conv)

#32
def preco(dist,dias):
    custo=260*dias+dist*0.15
    print('Preço total a pagar: R$%.2f'%custo)
    return

km=float(input('Quantidade de km percorridos: '))
day=int(input('Quantidade de dias alugados: '))

preco(km,day)

#33
def progress(t1,r,n):
    tn=t1+(r*(n-1))
    print('Termo',n,'=',int(tn))
    return

prime=float(input('Primeiro termo da PA: '))
razao=float(input('Razão da PA: '))
ene=int(input('Número do termo desejado: '))

progress(prime,razao,ene)



