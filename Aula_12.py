#LINK PARA O TUTOR PYTHON:  http://pythontutor.com/visualize.html#mode=edit
#Ajuda a analisar passo a passo a recursão

#exibir o numero verticalmente
def exibir(n):
    if n<10:
        print(n)
    else:       #tambem pode ser escrito na forma de return
        exibir(n//10)    #se nao for menor que 10, vai repetindo ate ir
        print(n%10)     #depois exibe o resto (fica congelado esperando imprimir o resto)
    return

exibir(326)

#exibir o numero ao contrario= fazer o mesmo de antes e trocar n//10 e n%10

#1    resolver com numero = usar // e %
def contAlg(n):
    if n<10:
        return 1
    else:
        c=contAlg(n//10)
        return 1+c   #vai contar o numero de algarismos(pois vai somando 1 a cada)

#2
def cont2(n):
    if n<10:
        if n ==2:
            return 1
        else:
            return 0    #se nao tiver 2 nao conta com mais 1
    else:
        c=cont2(n//10)   #quantos numeros 2 tem no numero sem sua unidade?
        if n%10==2:
            return 1+c
        else:
            return c

num_2=cont2(12278)

#3
def contIgual(numero,algarismo):
    if numero<10:
        if numero==algarismo:
            return 1
        else:
            return 0
    else:
        c=contIgual(numero//10,algarismo)
        if numero%10==algarismo:
            return 1+c
        else:
            return c

v=contIgual(267797,7)

#4
def verifica(n):
    if n<10:
        if n==2:
            return True
        else:
            return False
    else:
        if n%10==2:
            return True
        else:
            c=verifica(n//10)
            return c


f=verifica(120)
            

        
    
                
            
    

        
            

        
