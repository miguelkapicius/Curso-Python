valor=float(input('Qual o valor do imóvel? '))
sal=float(input('Qual o salário? '))
anos=int(input('Quantos anos? '))
mensal= (valor/anos)/12
sal30= sal*0.30
if mensal>sal30:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
    