lista=[]
for n in range(0,5):
    v=int(input('Digite um valor: '))
    if n ==0 or v > lista[-1]:
        lista.append(v) 
    else:
        pos=0
        while pos< len(lista):
            if n <= lista[pos]:
                lista.insert(pos, v)
                break
            pos+=1
print('-='*30)
print(f'Os números digitados foram {lista}')
print('-='*30)