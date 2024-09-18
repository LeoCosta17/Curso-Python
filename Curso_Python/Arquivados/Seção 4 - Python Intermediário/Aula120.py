pessoa = {
    'nome': 'Leonardo',
    'sobrenome': 'Costa',
    'idade': 20,
    'altura': 1.85,
    'endereco': [
        {'rua': 'Paraná', 'numero': 398},
        {'rua': 'Dona Regina Michelin', 'numero': 30},
    ],
}

print(pessoa['nome'])

pessoa['nome'] = 'Brenda'

print(pessoa['nome'])

print(pessoa['sobrenome'])

del pessoa['sobrenome']

# print(pessoa['sobrenome']) -> Gera Key Error

if pessoa.get('sobrenome') is None:
    print('Não Existe')
