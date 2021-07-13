#Iremos trabalhar com dois casos a partir de agora

def calculaIMC(idade,peso,altura):
    imc=peso/(altura*altura)
    print('IMC:%.2f'%imc)
    if imc<18.5 or imc>24.9:
        if imc<18.5:
            print('Alerta! Abaixo do peso!')
        else:
            print('Alerta! Acima do peso!')
    else:
        print('Parabens!')
    return

calculaIMC(18,20,2.1)

#tambem pode ser escrito da maneira abaixo
'''
if imc<18.5:
    print('Alerta! Abaixo do peso!')
elif imc<24.9:
    print('Parabens!')
else:
    print('Alerta! Acima do peso!')
    '''
    
def menor (a,b,c):
    if a<b and a<c:
        m=a
    elif b<a and b<c:
        m=b
    else:
        m=c
    print(m)
    return 

menor(50,9,80)


def resultado_aluno(n1,n2):
    media=(n1+n2)/2
    print('Media:%.2f'%media)
    if media>=5.0:
        print('APROVADO')
    elif media<=3.0:
        print ('REPROVADO')
    else:
        if n1>n2:
            m=n1   #m é a maior nota
        else:
            m=n2
        minimo=10-m
        print('Em prova final e precisa de no minimo',minimo)
    return

resultado_aluno(2,6)

def nota_rio(largura,profundidade,velocidade):
    vazao=largura*profundidade*velocidade
    if largura<15 or profundidade<6:
        nota=0
    elif largura>30:
        nota=5+(vazao/2000)
    else:
        if vazao<5000:
            nota=5+(vazao/2700)
        else:
            nota=5+(vazao/2500)
    #print('Vazao:%6.d Nota:%.2f'%(vazao,nota))
    return nota

nota_rio(25,10,70)

def avalia_rio(l,p,vel):
    n=nota_rio(l,p,vel)
    if n>7.0:
        print('Alternativa viavel')
    return

largura=float(input('Qual a largura?'))
profundidade=float(input('Qual a profundidade?'))
velocidade=float(input('Qual a velocidade?'))
avalia_rio(largura,profundidade,velocidade)

def pegaString(x):
    met=len(x)//2
    if '-'in x:  #se tiver o traço em x, retornar segunda metade e depois primeira metade  
        y=x[met:]+'&'+x[:met]
    else:    #se nao tiver, faça o oposto
        y=x[:met]+'&'+x[met:]
    if 'a'<=y[0]<='z':   #se o primeiro caractere de y é minusculo, tornar maiusculo
        y=chr(ord(y[0])-ord('a')+ord('A'))+y[1:]
    if 'A'<=y[-1]<='z':  #se o ultimo caractere de y é maiusculo, tornar minusculo
        y=y[:len(y)]+chr(ord(y[-1])-ord('A')+ord('a'))
    return y
        
        

        
        
        
        


