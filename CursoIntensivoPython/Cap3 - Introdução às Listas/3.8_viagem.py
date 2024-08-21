lugares_viajar = [
    'Ubatuba',
    'Maldivas',
    'São Paulo',
    'Uruguai',
    'Chile'
]

for indice, lugar in enumerate(lugares_viajar):
    print(f'{indice} - {lugar}')

lista_ordenada = sorted(lugares_viajar)

print('---')

for indice, lugar in enumerate(lista_ordenada):
    print(f'{indice} - {lugar}')

print('---')

lugares_viajar.reverse()

for indice, lugar in enumerate(lugares_viajar):
    print(f'{indice} - {lugar}')