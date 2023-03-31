from random import randint
from time import sleep
from operator import itemgetter
jog={}
for n in range (1,5):
    v = randint(1,6)
    jog[f'Jogador{n}'] = v

for k, v in jog.items():
    sleep(1)
    print(f'{k} tirou {v} no dado')

rank={}
rank= sorted(jog.items(), key=itemgetter(1), reverse=True)
print('-='*10)

for i, v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')