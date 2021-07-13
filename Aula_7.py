Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> len('oi')
2
>>> n='ola'
>>> n[1]
'l'
>>> n[0]
'o'
>>> n[:]
'ola'
>>> s='Oie, tudo bem'
>>> (s[1]+s[2])*4
'ieieieie'
>>> s[1:3]*4
'ieieieie'
>>> #sao iguais os dois de cima
>>> alfabeto='abcdefghijklmnopqrstuvwxuz'
>>> meio=len(alfabeto)//2
>>> alfabeto[meio]
'n'
>>> import random
>>> help(random.choice)
Help on method choice in module random:

choice(seq) method of random.Random instance
    Choose a random element from a non-empty sequence.

>>> help(random.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

>>> random.choice(alfabeto)
'r'
>>> random.choice(alfabeto)
'g'
>>> alfabeto[random.randint(0,len(alfabeto)-1)]
'x'
>>> #-1 porque na contagem so vai ate 25, ja que comeca com 0
>>> #duas maneiras de pegar uma letra do alfabeto aleatoriamente
>>> def f(x,y)
SyntaxError: invalid syntax
>>> from math import cos
>>> cos(90)
-0.4480736161291701
>>> math.cos(90)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    math.cos(90)
NameError: name 'math' is not defined
============== RESTART: C:/Users/PUC/Documents/aularascunho.py ==============
>>> senha
'03$03#30!30*1961'
>>> import math
============== RESTART: C:/Users/PUC/Documents/aularascunho.py ==============
>>> percentual
2.499999999999991
