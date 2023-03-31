import random
from time import sleep
nums=[]
jogos=[]
tot=1
print('-='*15)
print('{:^30}'.format('MEGA SENA'))
print('-='*15)
e= int(input('Quantos jogos você quer que eu sorteie? '))
while tot<=e:
    cont=0
    while True:
        n= random.randint(1,60)
        if n not in nums:
            nums.append(n)
            cont+=1
        if cont==7:
            break
    nums.sort()
    jogos.append(nums[:])
    nums.clear() 
    tot+=1
print('-='*2, f'Sorteando {e} jogos', '-='*2) 
for i, j in enumerate(jogos):
    print(f'Jogo {i+1}: {j}') 
    sleep(1)
print('-='*15)
