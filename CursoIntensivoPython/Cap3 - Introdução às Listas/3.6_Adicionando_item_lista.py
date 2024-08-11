lista_convidados = [
    'Abel Ferreira',
    'Felipão',
    'São Marcos',
    'Romário',
    'Rogério Ceni',
    'Weverton'
]

lista_convidados.insert(0, 'Caio Paulista')
lista_convidados.insert(4, 'Veiga')
lista_convidados.append('Anibal Moreno')

for index, name in enumerate(lista_convidados):
    print(f'`{index} - {name}')