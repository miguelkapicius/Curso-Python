preco=float(input('Qual o valor do produto? R$'))
desc= preco*0.05
final= preco-desc
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}'.format(preco,final))