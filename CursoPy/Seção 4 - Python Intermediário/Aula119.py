pessoa = {
    'nome': 'Leonardo',
    'idade': 20,
    'altura': 1.85
}

print(pessoa, type(pessoa))
print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])