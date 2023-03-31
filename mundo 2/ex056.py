cont=0
nomevelho=''
media=0
soma=0
for pess in range(1,5):
    nome=str(input('Digite o nome da {}° pessoa: '.format(pess)))
    idade=int(input('Digite a idade da {}° pessoa: '.format(pess)))
    sexo=str(input('Qual o sexo da {}° pessoa? (H) ou (M)'.format(pess))).upper()
    if pess==1 and sexo=='H':
        velho=idade
        nomevelho=nome
    if idade>velho and sexo=='H':
        velho=idade
    if idade<20 and sexo=='M':
        cont=cont+1
    soma+=idade
    media=soma/4
print('A média de idade do grupo é {} anos'.format(media))
print('O homem mais velho é o {} com {} anos'.format(nomevelho, velho))
print('Tem {} mulheres com menos de 20 anos'.format(cont))