def voto(data):
    from datetime import date
    d= date.today().year - data
    if d < 16:
        print(f'Com {d} anos: Voto Negado.')
    elif 16<= d < 18 or d > 65:
       print(f'Com {d} anos: Voto Opcional')
    else:
        print(f'Com {d} anos: Voto Obrigatório')

        

    
n = int(input('Digite o ano de nascimento: '))
voto(n)