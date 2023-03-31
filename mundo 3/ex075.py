cont=0
valor = (int(input('Primeiro valor:')),
        int(input('Segundo valor:')),
        int(input('Terceiro valor:')),
        int(input('Quarto valor:')))

print(f'Os valores são {valor}')
print(f'O valor 9 apareceu {valor.count(9)} vezes')
if 3 in valor:
    print(f'O valor 3 aparece primeiro na {valor.index(3)+1}ª posição')
else:
    print('O valor 3 não está presente')
print(f'Os valores pares foram ', end='')
for n in valor:
    if n%2==0:
        print(n, end=' ')