n1=float(input('Primeiro valor: '))
n2=float(input('Segundo valor: '))
maior=0
opcao=0
while opcao!= 5:
    print('''O que deseja fazer com eles?
    [1] somar
    [2] multiplicar
    [3] saber o maior
    [4] novos números
    [5] sair do programa''')
    opcao=int(input('>>>>Qual a opção desejada? '))
    if opcao==1:
        soma= n1+n2
        print('A soma dos dois itens é {}'.format(soma))
    elif opcao==2:
        mult= n1*n2
        print('A multiplicação dos dois é {}'.format(mult))
    elif opcao==3:
        if n1>n2:
            maior=n1
            print('O maior número é {}'.format(maior))
        elif n1<n2:
            maior=n2
            print('O maior número é {}'.format(maior))
        else:
            print('São iguais')
    elif opcao==4:
        print('Informe os novos números!')
        n1=float(input('Primeiro valor: '))
        n2=float(input('Segundo valor: '))
    elif opcao==5:
        print('Encerrando programa')
    else:
        while opcao>5:
            print('Essa opção não existe!')
            opcao=int(input('Digite uma das opções de 1 a 5: '))
