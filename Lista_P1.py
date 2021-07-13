#REVISAO P1

#1
def ehMultiplo(n1,n2):
    if n1%n2==0:
        return True
    else:
        return False

def algarismoDigitoVerificador(pb):
    if ehMultiplo(pb,2):
        unidade=pb%8
    else:
        unidade=pb%7
    return unidade

def parteBaseDigitoVerificador(num):
    partebase=(num//100)*8+((num%100-num%10)//10)*4+num%10*3
    return partebase

def digitosVerificadores(n):
    y=algarismoDigitoVerificador(parteBaseDigitoVerificador(n%1000))
    x=algarismoDigitoVerificador(parteBaseDigitoVerificador(n//1000))
    return x*10+y

b=digitosVerificadores(1002)
print(b)

#2
def inverte(s):
    return s[-1]+s[1:len(s)-1]+s[0]

def replicata(s):
    return 3*(s[0]+s[-1])

def criaSenha(nome,sobrenome):
    parte1=replicata(nome)
    prefixo=inverte(nome[len(nome)//2:])
    sufixo=inverte(nome[:len(nome)//2])
    if nome in sobrenome:
        senha=parte1+sobrenome
    elif ' ' in nome:
        senha=prefixo+sobrenome+sufixo
    else:
        senha=prefixo+sobrenome[::-1]+sufixo
    return senha

c=criaSenha('Margarida','Disney')
print(c)

#3
def criaString(s):
    return s+4*(s[0]+s[1]+s[-1]+s[-2])

d=criaString('abcdefg')
print(d)

#4    DUVIDAAA
def qtAlg(s):
    if not s:
        return -1
    elif s[0]=='@':
        return 0
    else:
        r=qtAlg(s[1:])
        if r==-1:
            return -1
        else:
            if s[0] in "0123456789":
                r=1+qtAlg(s[1:])
            else:
                r=qtAlg(s[1:])
    return r
print(qtAlg("dshvfdsgh234fxv34"))

#5
def vertical(n):
    if n<10:
        print(n)
    else:
        vertical(n//10)
        print(n)
    return

vertical(1234)
        
#6

def concatena(s1,s2):
    if not s1:
        return s2
    if not s2:
        return s1
    return s1[0]+s2[0]+concatena(s1[1:],s2[1:])

a=concatena('local','misterio')
print(a)

#7
def bonusCliente(valor_uc,tempo):
    if tempo>6:
        bonus=5/100*valor_uc
    elif tempo<=3:
        bonus=20/100*valor_uc
    else:
        bonus=10/100*valor_uc
    return bonus

def calculaValorComBonus(valor_ucompra,meses,valor_atual):
    if bonusCliente(valor_ucompra,meses)>valor_atual:
        vpago=0
    else:
        vpago=valor_atual-bonusCliente(valor_ucompra,meses)
    return vpago

vatual=float(input('Valor de compra atual: '))
vultimo=float(input('Valor da ultima compra: '))
dura=int(input('Quantos meses da ultima compra: '))

v=calculaValorComBonus(vultimo,dura,vatual)
print('Valor pago pelo cliente = R$ %.2f'%v)

#8
def repeteAlg(s):
    if not s:
        return ''
    else:
        if s[0] in '1234567890':
            return s[0]+s[0]+repeteAlg(s[1:])
        else:
            return s[0]+repeteAlg(s[1:])

r=repeteAlg('2prog1')
print(r)

#9
def contIgual(s1,s2):
    if (not s1 and s2) or (not s2 and s1):
        return False
    elif not s1 and not s2:
        return True
    elif s1[0]!=s2[0]:
        return False
    else:
        return contIgual(s1[1:],s2[1:])

i=contIgual('Daniel','Daniel')
print(i)

#10
def prefixo(s1,s2):
    if not s1 and s2:
        return True
    elif s1[0]!=s2[0]:
        return False
    else:
        if s1[0]==s2[0]:
            return prefixo(s1[1:],s2[1:])


p=prefixo('Anão','Anarquia')
print(p)

        

