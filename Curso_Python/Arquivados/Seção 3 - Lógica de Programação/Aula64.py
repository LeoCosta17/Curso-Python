nome = 'Leonardo'
index_nome = 0
tam_nome = len(nome)

novo_nome = ''
while index_nome < tam_nome:
    print(nome[index_nome])
    novo_nome += (nome[index_nome] + 'B')
    index_nome += 1

print(novo_nome)