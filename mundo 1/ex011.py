# 2m² = 1L tinta
larg=float(input('Largura da parede: '))
altu=float(input('Altura da parede: '))
area= larg*altu
litros= area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg,altu,area))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(litros))
