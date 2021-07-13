#13
def calcDesconto(valor,perc):
    desconto=(perc/100)*valor
    return desconto

def valores(quant,unit):
    vtotal=quant*unit
    if quant>15 and vtotal>100.00:
        vpago=vtotal-calcDesconto(vtotal,10)-calcDesconto(vtotal-calcDesconto(vtotal,10),20)
    elif quant>15 and vtotal<=100:
        vpago=vtotal-calcDesconto(vtotal,10)
    elif quant<=15 and vtotal>100:
        vpago=vtotal-calcDesconto(vtotal,20)
    else:
        vpago=vtotal
    print('Valor total da compra = R$%.2f Valor pago pelo cliente = R$%.2f'%(vtotal,vpago))
    return

quant1=int(input('Quantidade do produto: '))
unit1=float(input('Valor unitario do produto em reais: '))

valores(quant1,unit1)
        
#16

def preco_venda(gm,tc,cmo,ac):
    if (ac/tc)<0.035:
        cmo=(130/100)*cmo
    ct=gm+cmo*tc
    if gm/(cmo*tc)>1.5:
        lucro=(5/100)*gm
    elif gm/(cmo*tc)>=0.5:
        lucro=(8/100)*ct
    else:
        lucro=(10/100)*(cmo*tc)
    venda=ct+lucro
    print('Preço de venda do imóvel = R$%.2f'%venda)
    return

gm1=float(input('Valor gasto com o material: '))
tc1=float(input('Tempo de duração da construção em horas: '))
cmo1=float(input('Custo por hora da mão de obra: '))
ac1=float(input('Metragem da area construída em m2: '))

preco_venda(gm1,tc1,cmo1,ac1)

#18

def DiaDaSemana(dia,mes,ano):
    A=ano-1900
    B=A//4
    if A%4==0 and (mes=='fevereiro' or mes=='janeiro'):
        B=B-1
    if mes=='janeiro'or mes=='outubro':
        C=0
    elif mes=='maio':
        C=1
    elif mes=='agosto':
        C=2
    elif mes=='junho':
        C=4
    elif mes=='setembro' or mes=='deembro':
        C=5
    elif mes=='abril' or mes=='julho':
        C=6
    else:
        C=3
    D=dia-1
    S=A+B+C+D
    R=S%7
    return R

print(DiaDaSemana(11,'agosto',2000))

#21



#22
