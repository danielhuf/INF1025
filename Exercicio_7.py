#1
def contAlg(n):
    if n<10:
        if n==3 or n==4:
            return 1
        else:
            return 0
    else:
        if n%10==3 or n%10==4:
            return 1+contAlg(n//10)
        else:
            return contAlg(n//10)

print(contAlg(239424))

#2
def converte(n):
    if n<10:
        return str(n)
    else:
        return converte(n//10)+str(n%10)

print(converte(1950))
print(type(converte(1950)))

#3
def contOrdem(n1,n2):
    if n1<10 and n2<10:
        if n2<=n1:
            return False      #é bom sempre começar com as sentenças falsas,
        else:                 #porque quando chega no True meio que "para"
            return True
    else:
        if n2%10<=n1%10:
            return False
        else:
            return contOrdem(n1//10,n2//10)

print(contOrdem(1234,2456))
print(contOrdem(1234,2436))

#4
def vert(n):
    if n<10:
        print(n)
    else:
        vert(n//10)
        print(n%10)

vert(198)


#5
def invert(n):
    if n<10:
        print(n)
    else:
        print(n%10)
        vert(n//10)

vert(198)

#8
def suprime(n,a):
    if n<10:
        if n==a:
            return 0
        else:
            return n
    else:
        if n%10==a:
            return suprime(n//10,a)
        else:
            return (suprime(n//10,a)*10)+n%10

print(suprime(12342,2))

#13
def presente(s,a):
    if not s:
        return False
    else:
        if s[0]==a:
            return True
        else:
            return presente(s[1:],a)

print(presente('daniel','d'))

#14
def contFreq(s,a):
    if not s:
        return 0
    else:
        if s[0]==a:
            return 1+contFreq(s[1:],a)
        else:
            return contFreq(s[1:],a)

print(contFreq('Amadora','a'))
print(contFreq('Amadora','k'))

#16
def piramide(s):
    if len(s)==1:
        print(s)
    else:
        print(s)
        piramide(s[1:])

piramide('Cana')
piramide('abcdefghijklmnopqrstuvwxyz')

#21
def invertpar(s):
    if not s:
        return ''
    if len(s)==1:
        return s
    else:
        return s[1]+s[0]+invertpar(s[2:])

print(invertpar('abcde'))

#25
def inverte(s):
    if not s:
        return ''
    else:
        return inverte(s[1:])+s[0]

print(inverte('Teste'))

#29     #NAO SEI FAZER TIRANDO OS ESPAÇOS E TRAÇOS
def palindromo(s):
    if not s:
        return False
    if s[0]!=s[-1]:
        return False
    else:
        palindromo(s[1:-1])
        return True

print(palindromo('ahrrha'))

#30
def vizinhos_iguais(s):
    if len(s)<=1:
        return 0
    else:
        if s[0]==s[1]:
            return 1+vizinhos_iguais(s[1:])
        else:
            return vizinhos_iguais(s[1:])

print(vizinhos_iguais('aajbb2cceccd'))

#31
def dois_iguais(s):
    if len(s)<=1:
        return 0
    else:
        if s[0]==s[1]:
            return 1+dois_iguais(s[2:])
        else:
            return dois_iguais(s[2:])

print(dois_iguais('aajbb2cceccd'))

#32   #NAO CONSEGUI COMPLETAR COM O VALOR DO INDICE
def ocorre(s,a):
    if not s:
        return -1
    else:
        if s[0]==a:
            return 0     #nesse caso eu preciso descobrir como colocar o numero do indice
        else:
            return ocorre(s[1:],a)

print(ocorre('amor','o'))

    



        

