import random
i1=input('Primeiro aluno ')
i2=input('Segundo aluno ')
i3=input('Terceiro aluno ')
i4=input('Quarto aluno ')
lista=[i1,i2,i3,i4]
escolhido=random.choice(lista)
print('O escolhido foi {}'.format(escolhido))
