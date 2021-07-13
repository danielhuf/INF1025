#1
def calcula_percent(valor,percent):
    return valor*percent/100

#a)
def calcula_com_taxas(vbasico):
    importa=calcula_percent(vbasico,50)
    circu=calcula_percent(vbasico+importa,3)
    entrega=calcula_percent(vbasico,10)+calcula_percent(circu,2)
    return vbasico+importa+circu+entrega

#b)
def calcula_com_taxas(vbasico):
    importa=calcula_percent(vbasico,50)
    circu=calcula_percent(vbasico+importa,3)
    entrega=calcula_percent(vbasico,10)+calcula_percent(circu,2)
    valor=str(vbasico)
    taxas=str(importa+circu+entrega)
    vtotal=str(vbasico+importa+circu+entrega)
    vpercentual=str(((vbasico+importa+circu+entrega)/vbasico)*100)
    return str('Valor Basico R$'+valor+' Taxas:'+taxas+' Valor Total:'+vtotal+' Percentual de taxas: '+vpercentual+'%')

a= calcula_com_taxas(50)

#c)
def valor_a_pagar(codigo):
    pbasico=(codigo//100)*15+(codigo%100)   #//100 ira pegar os dois primeiros algarimso do numero de 4 digitos
    pdesconto=codigo%100    #%100 ira pegar os ultimos dois algarismos do numero de 4 digitos
    total=pbasico-calcula_percent(pbasico,pdesconto)
    print('Total a pagar',total)
    return

valor_a_pagar(2314)

#d)
def valordaFantasia(metragem,preco_metro):
    custo=calcula_percent((metragem*preco_metro),30)
    preco_venda=calcula_percent(custo,110)
    return preco_venda

#o resto da questao nao está bem formulado

#e)
def calculaNota(nespecifico,ngeral,nmat,nport):
    c1=calcula_percent(nespecifico,40)
    c2=calcula_percent(ngeral,20)
    c3=calcula_percent(nmat,15)
    c4=calcula_percent(nport,25)
    nfinal=c1+c2+c3+c4
    return nfinal

c=calculaNota(80,40,80,65)

#2
#a)
def areaQuadrado(l):
    return l*l

#b)
def areaCadeira(l):
    areaOcupada=(110/100)*areaQuadrado(l)
    return areaOcupada

#c)
def numeroCadeiras(lterreno,lpiscina,lcadeira):
    num_cadeiras=(areaQuadrado(lterreno)-areaQuadrado(lpiscina))//areaCadeira(lcadeira)
    return num_cadeiras

d=numeroCadeiras(40,20,1)

#3
#a)
def soma_dig(n):
    a1=n//10
    a2=n%10
    return a1+a2

#b)
def criaSenha(dia,mes,ano):
    a=soma_dig(dia)
    b=soma_dig(mes)
    c=soma_dig(ano%100)
    senha=str(a)+str(b)+str(c)
    return senha

e=criaSenha(27,3,1999)

#4) 
def centraliza(string,tamlinha):
    espacodolado=(tamlinha-int(len(string)))//2
    esquerda=(' ')*espacodolado
    direita=(' ')*espacodolado
    return esquerda+string+direita

q= centraliza('João Pé de Feijão',50)

#5) JA FOI FEITA EM ALGUM SLIDE DA AULA

#6)
def fazerFracao(numerador,denominador):
    num=str(numerador)
    den=str(denominador)
    div=str(numerador/denominador)
    return num+'/'+den+'='+div

f=fazerFracao(10,2)

#7)
import math
def calculaLog(logaritmo,base):
    return math.log(logaritmo,base)

g=calculaLog(32,2)


#8) JA FOI FEITA NA LISTA 2 PARA O TESTE

#9)
def converte(hora,minuto):
    total_minutos= hora*60+minuto
    return total_minutos

def calcula_dif(hora1,minuto1,hora2,minuto2):
    total_minutos1=converte(hora1,minuto1)
    total_minutos2=converte(hora2,minuto2)
    dif_minutos=total_minutos1-total_minutos2
    return dif_minutos

def monta_horario(quant_minutos):
    horas=str(quant_minutos//60)
    minutos=str(quant_minutos%60)
    return horas+'h'+minutos+'m'

def monta_hora(prim_hora,prim_minuto,seg_hora,seg_minuto):
    return monta_horario(calcula_dif(prim_hora,prim_minuto,seg_hora,seg_minuto))

h=monta_hora(3,20,1,5)
    

#10) JA FOI FEITA NA LISTA 2 PARA O TESTE

#11) JA FOI FEITA EM ALGUM SLIDE DA AULA

#12)
def boasvindas(nome,idade):
    x=str(2*idade)
    return 'Olá '+nome+', meu nome é Python e eu tenho '+x+' anos'

i=boasvindas('Daniel',17)

#13)
def concatena(string1,string2):
    s=string1[5:]
    t=string2[:len(string2)-10]
    return s+t

j=concatena('12345678901234567890','abcdefghijklmnopqrstuvwxyz')

#14)
def mudaposicao(s,x,i):
    return s[:i]+x+s[i+1:]

k=mudaposicao('Daniel','b',2)

#15)
def hashtag(string):
    p=int(len(string)/2)
    return '#'+string[:p]+'#'+string[p:]+'#'

l=hashtag('abcde')


#16)
def numero_de_letras(nome):
    return len(nome)

b=numero_de_letras('daniel')

#17)
def mudanome(nome):
    return nome[1]+nome[int(len(nome)//2-1)]+nome[int(len(nome)-2)]

m=mudanome('Daniel')
#n=mudanome('D')    DEU OUT OF RANGE

#18)
def juntastring(string1,string2):
    return string1[1:]+string2[int(len(string2)-1):0:-1]

o=juntastring('abcd','mnopq')

#19)
def replicata(string):
    concatena=4*(string[0]+string[1]+string[int(len(string)-1)]+string[int(len(string)-2)])
    return string+concatena

r=replicata('abcdefg')




