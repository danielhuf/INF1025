def contMai(s):
    if s=='':     #ou if not s (significa que a string é vazia
        return 0
    else:
        if 'A'<=s[0]<='Z':
            t=1
        else:
            t=0
        return t+contMais(s[1:])     #contará o t da primeira e o t dos outros carcateres da string

#Maneira mais elegante de escrever essa funcao
def contMaiu(s):
    if not s:
        return 0
    else:
        if 'A'<=s[0]<='Z':
            return 1+contMaiu(s[1:])
        else:
            return contMaiu(s[1:])

print(contMaiu('FiM'))

#1
def exibeVert(s):
    if not s:      #not é para se o s é vazio
        return
    else:
        print(s[0])
        exibeVert(s[1:])
        return

exibeVert('Daniel')

#2
def repete(s):
    if not s:
        return ''
    else:
        return s[0]+s[0]+repete(s[1:])

a=repete('prog1')

print(a)

#3
def vogal(s):
    if not s:
        return ''
    else:
        if s[0] in "aeiouAEIOU":
            return s[0]+s[0]+vogal(s[1:])
        else:
            return s[0]+vogal(s[1:])

b=vogal('carro')
print(b)

#4
def substitui(s):
    if not s:
        return ''
    else:
        if s[0] == ' ':    #tem que colocar espaço entre aspas para reconhecer que há espaço
            return '#'+substitui(s[1:])
        else:
            return s[0]+substitui(s[1:])

c=substitui('dan i el')
print(c)

#EXTRA contar quantos digitos tem uma string?

def contDig(s):
    if not s:
        return 0
    else:
        if s[0] in '0123456789':
            return 1+contDig(s[1:])
        else:
            return contDig(s[1:])

d=contDig('dan123huf82')
print(d)

#5    #O DA PROFESSORA ESTA DANDO ERRADO
def contSub(s1,s2):
    if s2=='':
        return 1
    if not s1:
        return 0
    if s1[0]==s2[0]:
        return contSub(s1[1:],s2[1:])+contSub(s1[1:],s2)
    return contSub(s1[1:],s2)

h=contSub('Daaaaniel','an')
print(h)

#6
def contc(s,k):
    string=s[k:]
    if not string:
        return 0
    else:
        if string[0]=='c':
            return 1+contc(string[1:],0)
        else:
            return contc(string[1:],0)

e=contc('arcondicionadoc',4)
print(e)


                          



