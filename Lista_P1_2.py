#1
'''
def determina_valorKWH(tipo,cor):
    if cor=='verde':
        valor=3.20
    elif cor=='amarela':
        valor=4.50
    else:
        if tipo==1:
            valor=6.00
        else:
            valor=5.00
    return valor

def calcula_TaxaExtra(valor_conta,tipo_user):
    if tipo_user==1:
        taxa=50/100*(valor_conta)
    else:
        num_func=int(input('Número de funcionários: '))
        if num_func>100:
            taxa=2/100*(valor_conta)
        else:
            taxa=3/100*(valor_conta)
    return taxa

def calcula_conta(bandeira,usuario,val_KWH,consumo_mensal):
    if bandeira=='amarela' or 'vermelha':
        t_extra=calcula_TaxaExtra(val_KWH*consumo_mensal,usuario)
    else:
        t_extra=0
    total=val_KWH*consumo_mensal+t_extra
    print('Total a pagar = R$%.2f'%total)
    return

band=input('Cor da bandeira: ')
user=int(input('Usuário (1 para residencial e 2 para não residencial): '))
cons=float(input('Consumo mensal em KWH: '))

val=determina_valorKWH(user,band)

calcula_conta(band,user,val,cons)

#2
def separaTipo(s):
    if not s:
        return ''
    elif s[0] in 'aeiouAEIOU':
        return s[0]+separaTipo(s[1:])
    else:
        return separaTipo(s[1:])+s[0]

print(separaTipo('curado'))

#3
def valorVenda(idade,horario,quant,preco):
    if '08:00'<=horario<='09:30':
        if idade<60:
            desconto=80/100
        else:
            desconto=70/100
        custo=((quant//3)*3)*preco*desconto+(quant%3)*preco
    else:
        custo=quant*preco
    print('Valor da venda = R$ %.2f'%custo)
    return

ida=int(input('Idade: '))
hora=input('Horário da venda no formato hh:mm')
qua=int(input('Quantidade vendida: '))
pre=float(input('Preço unitário: '))

valorVenda(ida,hora,qua,pre)

#4
def geraSenha(nome,idade,data):
    if idade>=40:
        miolo='&@'
    elif idade<=18:
        miolo='#*'
    else:
        miolo='$%'
    senha_acesso=nome[0]+nome[-1]+miolo+data[-1:-3:-1]
    return senha_acesso

print(geraSenha('Luiz Felipe',25,'19/04'))

#5
def converteDZ(s):
    if len(s)==2:
        return s[1]
    else:
        v=s[1]+converteDZ(s[2:])
        return v

print(int(converteDZ('F1F8F0F5')))

#6
def quant_bolsas(area,vagas,semestre):
    if area=='H':
        if semestre==1:
            enem=(2/100)*vagas
            vestib=(3/100)*vagas
        else:
            enem=(3/100)*vagas
            vestib=(1/100)*vagas
    else:
        if semestre==1:
            enem=(3/100)*vagas
            vestib=(4/100)*vagas
        else:
            vestib=(5/100)*vagas
            bc=int(input('Quantidade de bolsas convenio = '))
            if bc>0:
                enem=0
            else:
                enem=(1/100)*vagas
    print('Quantidade de bolsas distribuídas: ENEM=%d vagas e Vestibular=%d vagas'%(enem,vestib))
    return

ar=input('Área de conhecimento(H para humanas e E para exatas): ')
vag=int(input('Numero de vagas oferecidas: '))
sem=int(input('Semestre alvo (1 ou 2): '))

quant_bolsas(ar,vag,sem)

#7
def substituiChar(s,c1,c2):
    if not s:
        return ''
    else:
        if s[0]==c1:
            return c2+substituiChar(s[1:],c1,c2)
        else:
            return s[0]+substituiChar(s[1:],c1,c2)

print(substituiChar('Rio de Janeiro','i','#'))
'''
#8
def dentro_do_horario(h1,h2):
    if h1<=h2:
        return True
    else:
        return False

def custo(hora,sexo,cupons):
    if sexo=='h':
        if hora<='18:00':
            ingresso=50
        elif hora>'20:00':
            ingresso=80
        else:
            ingresso=70
    else:
        if hora<='18:00':
            ingresso=50
        else:
            ingresso=60
    if dentro_do_horario(hora,'20:00'):
        niver=input('Data de aniversario no formato dd/mm: ')
        if niver=='25/04':
            cupons=cupons-1
        if cupons<=5:
            custo_bebida=cupons*8
        else:
            custo_bebida=5*8+((cupons-5)*20)
    else:
        custo_bebida=cupons*20
    
    print('Custo do ingresso = R$%.2f e custo da bebida = R$%.2f'%(ingresso,custo_bebida))
    return

h=input('Horario de entrada no formato hh:mm = ')
s=input('Sexo (m para homens e f para mulheres) = ')
c=int(input('Numero de cupons de bebidas: '))

custo(h,s,c)


        

            
            
    
