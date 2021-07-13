#1

esf10=0
esf15=0
esf20=0
esf25=0
cod=int(input('Código do brinquedo: '))

while cod>=0:
   A=float(input('Comprimento da caixa em cm: '))
   B=float(input('Largura da caixa em cm: '))
   C=float(input('Altura da caixa em cm: '))
   diagonal=(A**2+B**2+C**2)**(1/2)
   if diagonal<=10:
      esfera=10
      esf10+=1
   elif diagonal<=15:
      esfera=15
      esf15+=1
   elif diagonal<=20:
      esfera=20
      esf20+=1
   elif diagonal<=25:
      esfera=25
      esf25+=1
   else:
      print('Necessita-se de uma esfera maior para embalar')
   if diagonal<=25:
      print('Diâmetro da esfera que embalará o brinquedo = %d cm'%esfera)
   cod=int(input('Código do brinquedo: '))

print('%d embalagens com 10cm de diâmetro'%esf10)
print('%d embalagens com 15cm de diâmetro'%esf15)
print('%d embalagens com 20cm de diâmetro'%esf20)
print('%d embalagens com 25cm de diâmetro'%esf25)

#2

def Calcula_Prêmio(dp,dn):
   dia_promo=int(dp[:2])
   mes_promo=int(dp[3:])
   dia_user=int(dn[:2])
   mes_user=int(dn[3:])
   if dia_user==dia_promo and mes_user==mes_promo:
       premio=30*(dia_promo+mes_promo)
   elif mes_user==mes_promo:
        premio=20*(mes_promo)
   elif dia_user==dia_promo:
        premio=0.50*(dia_promo)
   else:
        premio=0
   return premio

promo=input('Data da promoção no formato dd/mm: ')
n_premiados=0
v_total=0

user=input('Data de nascimento do participante no formato dd/mm: ')
while user!='00/00':
    valor=Calcula_Prêmio(promo,user)
    if valor>0:
        print('Valor do prêmio = R$%.2f'%valor)
        n_premiados+=1
        v_total+=valor
    user=input('Data de nascimento do participante no formato dd/mm: ')

print('Quantidade de pessoas premiadas = %d'%n_premiados)
print('Valor total distribuído na promoção = R$%.2f'%v_total)
    
    
        
