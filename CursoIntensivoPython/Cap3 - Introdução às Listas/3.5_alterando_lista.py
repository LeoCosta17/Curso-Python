lista_convidados = [
    'Abel Ferreira',
    'Felipão',
    'São Marcos',
    'Romário',
    'Rogério Ceni',
    'Weverton'
]

for name in lista_convidados:
    print(f'{name}, gostaria de convidá-lo para minha festa!')

print(f'Não irá ao jantar: {lista_convidados[3]}')

lista_convidados[3] = 'Cristiano Ronaldo'

print(f'Novo convidado: {lista_convidados[3]}')

for name in lista_convidados:
    print(f'{name}, gostaria de convidá-lo para minha festa!')