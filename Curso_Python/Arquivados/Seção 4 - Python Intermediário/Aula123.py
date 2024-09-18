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

print(pessoa.get('sobrenome'))

nome = pessoa.get('nome')

print(nome)

end = pessoa.pop('endereco')

print(pessoa)

pessoa.popitem()

print(pessoa)

pessoa.update(nome = 'Teste', idade = 50, endereco = 'Araras')

print(pessoa)

tupla = ('nome', 'Brenda'), ('namorado', 'Leonardo')

pessoa.update(tupla)

print(pessoa)