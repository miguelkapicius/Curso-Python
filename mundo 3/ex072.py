n=int(input('Digite um número entre 0 e 20: '))
while n>20:
    n=int(input('Tente novamente. Digite um número entre 0 e 20: '))
exten= ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', ' doze', 'treze', 'catorze', 'quinze', 'dezeseis','dezesete', 'dezoito', 'dezenove', 'vinte')
print(f'Você digitou o número {exten[n]}')
