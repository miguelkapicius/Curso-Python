n=int(input('Digite um número inteiro: '))
print('''Escolha uma das opções de conversão:
[1] binário
[2] octal
[3] hexadecimal''')
opcao= int(input('Sua opção: '))
if opcao==1:
    print('{} convertido para Binário é igual a {}'.format(n, bin(n)))
elif opcao==2:
    print('{} convertido para Octal é igual a {} '.format(n, oct(n)))
elif opcao==3:
    print('{} convertido para Hexadecimal é igual a {}'.format(n, hex(n)))
else:
    print('Opção inválida')
