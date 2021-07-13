#uso de condicional para ver se, através do calculo da media, o aluno sera aprovado
def testa_aprovado(n1,n2):
    media=(n1+n2)/2
    #usaremos o print com formato
    print('Media:%1.f'%media)
    if media>=5:
        if n1>3.0:
            if n2>3.0:
                print('está aprovado')
    return

testa_aprovado(10.0,3.0)
testa_aprovado(8.0,9.0)
testa_aprovado(2.0,3.4)

x=-10
if x<0:
    print('O numero negativo',x,'nao e valido aqui')
print('Continuemos')

'if (x%2)==0    é multiplo de 2?'

#outras condições relacionadas a media do aluno
def testa_aprovado2(n1,n2):
    media=(n1+n2)/2
    print('Media:%1.f'%media)
    if not (media>=5 and n1>=3 and n2>=3):
        print('está em final')
    return

testa_aprovado2(2.0,3.0)

def testa_aprovado3(n1,n2):
    media=(n1+n2)/2
    print('Media:%1.f'%media)
    if media<5 or n1<3 or n2<3:
        print('está em final')
        if (n1<2 or n2<2) and n2<n1:
            print('precisa de muita atencao!')
    return

testa_aprovado3(3.0,1.0)

#variavel booleana
print(5==5) 
print(2>5)  

print(type(True))
print(type('True'))

#se o triangulo for equilatero, booleano retorna true, se nao ira retornar false
def equilatero(L1,L2,L3):
    return (L1==L2==L3)

r=equilatero(2,2,3)
print(r)
s=equilatero(5,5,5)
print(s)

def isosceles_nao_equilatero(L1,L2,L3):
    return((L1==L2!=L3)or(L1!=L2==L3)or(L1==L3!=L2))

t=isosceles_nao_equilatero(2,2,2)
print(t)

#farei a mesma coisa chamando a funcao equilatero
def isosceles_nao_equilatero2(L1,L2,L3):
    return(L1==L2 or L2==L3 or L1==L3) and not equilatero(L1,L2,L3)

g=isosceles_nao_equilatero2(2,2,2)
print(g)

#funcao nao tera parametro
def testa_bissexto():
    ano=int(input('Escreva um ano:'))
    if ano%4==0 and (ano%100!=0 or ano%400==0):
        print('É bissexto')
    return

testa_bissexto()

#1
def exibeIMC(idade,altura,peso):
    imc=peso/(altura**2)
    print('imc:%2.d'%imc)
    if imc<18.5:
        print('abaixo do peso ideal!')
    return

exibeIMC(18,1.8,50)

#2
def exibeIMC(idade,altura,peso):
    imc=peso/(altura**2)
    print('imc:%2.d'%imc)
    if imc<18.5 and idade<18:
        print('menor está abaixo do peso ideal!')
    return

exibeIMC(17,1.8,100)

#3
def exibeIMC(idade,altura,peso):
    imc=peso/(altura**2)
    print('imc:%2.d'%imc)
    if imc<18.5 or imc>24.9:
        print('nao está no peso ideal!')
    return

exibeIMC(17,2.1,50)

#4
def exibeIMC(idade,altura,peso):
    imc=peso/(altura**2)
    print('imc:%2.d'%imc)
    if (idade<18 and imc<18.5) or (imc>24.9):
        print('nao está no peso ideal!')
    return

exibeIMC(17,1.8,50)

        
        



