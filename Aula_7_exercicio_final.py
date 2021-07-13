#1  função para gerar uma senha

def junta(x,y):
    return x+y[::-1]

def geraSenha(dia,mes,ano):
    s1=mes+'$'
    s2=junta(s1,dia)
    s3=s2+'#'+dia+'!'
    s4=junta(s3,mes)
    return s4+'*'+ano


date='30/03/1961'
dia=date[0:2]
mes=date[3:5]
ano=date[6:]
senha=geraSenha(dia,mes,ano)

#2  função para calcular o percentual em relação a um valor exato e um aproximado

def erro_absoluto(valor_exato,valor_aprox):
    return abs(valor_exato-valor_aprox)

def erro_relativo(valor_exato,valor_aprox):
    return erro_absoluto(valor_exato,valor_aprox)/valor_aprox

def erro_percentual(valor_exato,valor_aprox):
    return erro_relativo(valor_exato,valor_aprox)*100

exato=4.1
aproximado=4

percentual=erro_percentual(4.1,4)




