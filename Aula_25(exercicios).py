import random

p_luis=0
p_fern=0
rodada=1

while rodada<=11:
    print('RODADA',rodada)
    n_luis=random.randint(0,10)
    n_fern=random.randint(0,10)
    print('Número gerado para Luiz:',n_luis)
    print('Número gerado para Fernando:',n_fern)
    soma=n_luis+n_fern
    if soma%2==0:
        print('Luiz ganhou a rodada \n')
        p_luis+=1
    else:
        print('Fernando ganhou a rodada \n')
        p_fern+=1
    rodada+=1

if p_luis>p_fern:
    print('Luiz ganhou o jogo com %d rodadas vencidas.'%p_luis)
else:
    print('Fernando ganhou o jogo com %d rodadas vencidas.'%p_fern)
    
        
        
