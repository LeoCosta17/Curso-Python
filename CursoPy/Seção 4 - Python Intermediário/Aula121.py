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

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa.setdefault('sexo', 'masculino')
print(pessoa['sexo'])