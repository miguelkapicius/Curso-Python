frase=str(input('Digite uma frase: ')).strip() .upper()
palavras= frase.split()
junto= ''.join(palavras)
contrario= ''
for letra in range(len(junto)-1, -1, -1):
    contrario += junto[letra]
if contrario==junto:
    print(junto, contrario)
    print('Essa palavra é um palíndromo')
else:
    print(junto, contrario)
    print('Essa palavra não é um palíndromo')
    