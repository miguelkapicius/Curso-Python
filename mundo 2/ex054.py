from datetime import date
hoje= date.today().year
contmaior=0
contmenor=0
for pess in range(1,8):
    nasc=int(input('Digite a data de nascimento da {}° pessoa :'.format(pess)))
    if nasc>hoje-18:
        contmenor=contmenor+1
    else:
        contmaior=contmaior+1
print('Das 7 pessoas informadas, {} são maiores e {} são menores'.format(contmaior, contmenor))
