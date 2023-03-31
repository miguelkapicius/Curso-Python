classificação=('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
 'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
  'Botafogo', 'Santos', 'Goiás', 'Bragantino', 
  'Coritiba', 'Cuiabá', 'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')
print('-'*50)
print(f'Lista de times do Brasileirão: {classificação}')
print('-'*50)
print(f'Os 5 primeiros são {classificação[0:5]}')
print('-'*50)
print(f'Os 4 ultimos são {classificação[-4:]}')
print('-'*50)
print(f'Times em ordem alfabética: {sorted(classificação)}')
print('-'*50)
print(f'O Coritiba está na {classificação.index("Coritiba")+1}ª posição')

